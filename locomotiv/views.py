import math

import openpyxl as openpyxl
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from locomotiv.models import Locomotiv, TotalDataVagon, VagonResistanceConstant, TrainResistanceData, RailwaySwitchMark, \
    RailRoadCharacteristic, WeightModel
from locomotiv.serializers import NumberSerializer, LocomotivSerializer, TotalDataSerializer, InputDataSerializer, \
    InputSerializer, RailRoadSwitchSerializer, RailRoadCharacteristicSerializer, TrainRunningDistanceSerializer, \
    UploadVagonNumberSerializer
from locomotiv.utils import resistance_export_excel, find_total_resistance_vagon, find_total_number_of_pads, \
    find_sum_length_vagons, find_sum_brutto_vagon, find_locomotiv_traction_mode, find_locomotiv_idle_mode, \
    find_total_resistance_traction, find_total_resistance_idle, find_declivity_resistance, find_curvature_resistance, \
    find_curvature_resistance_for_switch, find_outside_temperature_resistance, find_wind_capacity_resistance, \
    find_vagons_ahead_resistance, find_railroad_condition_resistance, find_specific_idle_resistance, get_pulling_force, \
    get_vagon_data
from .wind_dict import get_wind_coefficient


class VagonDataListView(generics.CreateAPIView):
    queryset = Locomotiv.objects.all()
    serializer_class = NumberSerializer

    def get(self, *args, **kwargs):
        queryset = TotalDataVagon.objects.all()
        serializer = TotalDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        serializer = NumberSerializer(data=self.request.POST)
        serializer.is_valid(raise_exception=True)
        number = serializer.data['number']
        if number[0] == 0 or 1:
            return Response({"error_message": "Vagon raqami 0 yoki 1 bilan boshlanmasligi kerak"},
                            status=status.HTTP_400_BAD_REQUEST)
        load_weight = serializer.data['load_weight']
        full_data = get_vagon_data(number, load_weight)

        input_data = {
            'number_of_arrow': full_data['number_of_arrow'],
            'netto_vagon': full_data['netto_vagon'],
            'length_vagon': full_data['length_vagon']
        }
        input_serializer = InputDataSerializer(data=input_data)
        input_serializer.is_valid(raise_exception=True)

        serializer = TotalDataSerializer(data=full_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(full_data, status=status.HTTP_200_OK)


class UploadVagonNumberDataView(generics.GenericAPIView):
    serializer_class = UploadVagonNumberSerializer
    queryset = TotalDataVagon.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            file = self.request.FILES.get('file', None)
        except:
            return Response({
                "message": "File is not provided",
                "code": "bad_request"
            }, status=status.HTTP_400_BAD_REQUEST)
        if not file:
            return Response({
                "message": "File not found",
                "code": "not_found"
            }, status=status.HTTP_404_NOT_FOUND)
        dataframe = openpyxl.load_workbook(file)

        # Define variable to read sheet
        dataframe1 = dataframe.active

        # Iterate the loop to read the cell values
        for row in range(0, dataframe1.max_row):
            number = 0
            weight = 0
            i = 0
            if row == 0:
                continue
            for col in dataframe1.iter_cols(1, 2):
                if i == 0:
                    number = col[row].value
                else:
                    weight = col[row].value
                i += 1
                print(col[row].value)

            full_data = get_vagon_data(number, weight)
            serializer = TotalDataSerializer(data=full_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response('ok')


class LocomotivListListView(generics.ListAPIView):
    queryset = Locomotiv.objects.all()
    serializer_class = LocomotivSerializer
    search_fields = ['locomotiv_name', ]


class CalculateResultView(APIView):
    queryset = Locomotiv.objects.filter(is_active=True)

    # serializer_class = InputSerializer

    def post(self, request, find_specificc_idle_resistance=None, *args, **kwargs):
        global Kt, i, R, length_curvature, railway_characteristics, is_ahead, vagons_queryset, wind_capacity, outside_temperature, railway_switch, braking_time
        locomotiv_id = self.request.data.get('id')
        try:
            locomotiv = Locomotiv.objects.get(id=locomotiv_id)
        except:
            return Response({"error_message": "Bu idli lokomotiv mavjud emas!!!"}, status=status.HTTP_400_BAD_REQUEST)
        result = []
        for capacity in range(61):

            locomotiv_traction_mode = find_locomotiv_traction_mode(locomotiv, capacity)

            locomotiv_idle_mode = find_locomotiv_idle_mode(locomotiv, capacity)

            vagons_queryset = TotalDataVagon.objects.all()

            sum_brutto_vagon = find_sum_brutto_vagon(vagons_queryset)
            sum_length_vagons = find_sum_length_vagons(vagons_queryset)
            total_number_of_pads = find_total_number_of_pads(vagons_queryset)


            total_resistance_vagon = round(find_total_resistance_vagon(vagons_queryset, capacity))


            total_resistance_traction = find_total_resistance_traction(locomotiv, capacity, vagons_queryset)

            total_resistance_idle = find_total_resistance_idle(locomotiv, capacity, vagons_queryset)

            # additional resistances

            # Nishablikning solishtirma
            i = float(request.data.get('declivity'))
            Wi = find_declivity_resistance(i)

            # Egrilikning solishtirma qarshilik
            R = request.data.get('radius') or 0
            if R:
                R = float(R)
            length_curvature = request.data.get('length_curvature') or 0
            if length_curvature:
                length_curvature = float(length_curvature)
            Wor = find_curvature_resistance(R, length_curvature, locomotiv, vagons_queryset)

            # Strelkali o’tkazgichlarning solishtirma qarshiligi
            railway_switch = request.data.get('railway_switch_mark')
            if railway_switch is None:
                railway_switch = 0
                Wor_for_switch = 0
            else:
                railway_switch = int(railway_switch)
                Wor_for_switch = find_curvature_resistance_for_switch(railway_switch, locomotiv, vagons_queryset)

            # Past haroratning solishtirma qarshiligi
            outside_temperature = float(request.data.get('outside_temperature'))
            outside_temperature_resistance = find_outside_temperature_resistance(outside_temperature,
                                                                                 locomotiv, capacity, vagons_queryset)

            # Harakatga qarama qarshi va yon tomondan shamolning solishtirma qarshiligi
            wind_capacity = float(request.data.get('wind_capacity'))
            wind_capacity_resistance = find_wind_capacity_resistance(wind_capacity, capacity,
                                                                     locomotiv, vagons_queryset)

            # Vagonlar bilan oldinda harakatlangandagi solishtirma qarshilik
            is_ahead = request.data.get('is_ahead')
            Wvv = find_vagons_ahead_resistance(is_ahead, i, locomotiv, capacity, vagons_queryset)


            #  Yo’l holatining solishtirma qarshiligi

            railway_characteristics = int(request.data.get('railway_characteristic'))
            if railway_characteristics is None:
                railroad_condition_resistance = 0
            else:
                railroad_condition_resistance = find_railroad_condition_resistance(railway_characteristics,
                                                                               locomotiv, capacity, vagons_queryset)


            # Manoyvr tarkibining tortish rejimidagi harakatiga umumiy qarshilik.
            W = (locomotiv_traction_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
                        locomotiv.weigth + sum_brutto_vagon) *
                 (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
                  wind_capacity_resistance + Wvv + railroad_condition_resistance))

            # Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
            specific_traction_resistance = W / (locomotiv.weigth + sum_brutto_vagon)

            # Manyovr tarkibining salt rejimidagi harakatiga umumiy qarshilik
            Ws = (locomotiv_idle_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
                    locomotiv.weigth + sum_brutto_vagon) *
                  (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
                   wind_capacity_resistance + Wvv + railroad_condition_resistance))

            # Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
            specific_idle_resistance = Ws / (locomotiv.weigth + sum_brutto_vagon)

            data = {
                'capacity': capacity,
                "locomotiv_traction_mode": round(locomotiv_traction_mode, 2),
                'locomotiv_idle_mode': round(locomotiv_idle_mode, 2),
                'total_resistance_vagon': round(total_resistance_vagon, 2),
                'total_resistance_traction': round(total_resistance_traction, 2),
                'total_resistance_idle': round(total_resistance_idle, 2),

                'declivity_resistance': round(Wi, 2),
                'curvature_resistance': round(Wor, 2),
                'switch_curvature_resistance': round(Wor_for_switch, 2),
                'outside_temperature_resistance': round(outside_temperature_resistance, 2),
                'wind_capacity_resistance': round(wind_capacity_resistance, 2),
                'resistance_vagon_ahead': round(Wvv, 2),
                'railroad_condition_resistance': round(railroad_condition_resistance, 2),
                'all_traction_resistance': round(W, 2),
                'specific_traction_resistance': round(specific_traction_resistance, 2),
                'all_idle_resistance': round(Ws, 2),
                'specific_idle_resistance': round(specific_idle_resistance, 2)
            }
            TrainResistanceData.objects.create(**data)
            result.append(data)

        # saving locomotiv and vagons total weight
        sum_brutto_vagon = find_sum_brutto_vagon(vagons_queryset)
        WeightModel.objects.create(locomotiv_weight=locomotiv.weigth, vagons_weight=sum_brutto_vagon, locomotiv=locomotiv)

        # 3 - dastur uchun codelar

        is_magistral = request.data.get('is_magistral')

        # Lokomotivni bitta tormoz kolodkasinining o‘qga bosilishidagi haqiqiy kuchi
        total_lenght = locomotiv.lenght + find_sum_length_vagons(vagons_queryset)

        # tarkib umumiy og'irligi
        total_weight = locomotiv.weigth + find_sum_brutto_vagon(vagons_queryset)

        # tormoz berishdagi boshlangich tezlik
        V = self.request.data.get('brake_capacity', None)
        S = 0
        if V:
            V = round(float(self.request.data.get('brake_capacity')), 1)

            # 6-ustun uchun
            #  Lokomotivni bitta tormoz kolodkasinining o‘qga bosilishidagi haqiqiy kuchi
            K = 2300 * 2 * find_total_number_of_pads(vagons_queryset)

            braking_time = 1
            while V > 0:
                if is_magistral:
                    if total_lenght <= 500:
                        if braking_time < 27:
                            Kt = -0.0000191 * pow(braking_time, 3) - 0.000343 * pow(braking_time, 2) + 0.06 * braking_time
                        else:
                            Kt = 1
                    elif total_lenght > 500:
                        if braking_time < 33:
                            Kt = -0.0000255 * pow(braking_time, 3) - 0.000766 * pow(braking_time, 2) + 0.033 * braking_time
                        else:
                            Kt = 1  # Todo shu yerda barcha sanoat tarkibi uchun degan joyi qolib turadi
                else:
                    if braking_time < 31:
                        Kt = -0.0000107 * pow(braking_time, 3) - 0.00173 * pow(braking_time, 2) + 0.076 * braking_time
                    else:
                        Kt = 1

                # G'ildirakka tormoz kolodkasi ishqalanishning haqiqiy iqtisodiy koeffitsienti

                # 4-ustun uchun
                K1 = locomotiv.force_all_arrows * Kt

                Kv = Kt * K  # 6-ustun uchun

                # 5-ustun uchun
                p1 = 0.6 * (0.016 * locomotiv.force_per_arrow * Kt + 100) / (0.08 * locomotiv.force_per_arrow * Kt + 100) * (V + 100) / (5 * V + 100)

                # vagon uchun, 7-ustun
                p0 = 0.6 * (0.016 * 2300 * Kt + 100) / (0.08 * 2300 * Kt + 100) * (V + 100) / (5 * V + 100)

                # 8-ustun uchun
                # umumiy tormoz kuchi
                Vmt = Kv * p0 + K1 * p1
                # maryovr tarkibining salt yurish rejimidagi solishtirma qarshiligi
                specific_idle_resistance = find_specific_idle_resistance(locomotiv, V, vagons_queryset, i, R, length_curvature,
                                  railway_switch, outside_temperature, wind_capacity, is_ahead, railway_characteristics)

                # 10 - ustun uchun
                # manyorvr tarkibining umumiy solishtirma tormozlanish kuchi
                r = i + specific_idle_resistance + Vmt / total_weight

                # 11 - ustun
                # tezlik kamayishi
                delta_capacity = r / 30

                # 12 - ustun uchun
                # o'rtacha tezlik
                avg_capacity = V - round(delta_capacity / 2, 2)

                # 13 - ustun uchun
                # yurilgan yol jami
                S += avg_capacity / 3.6

                # vaqt o'tishi
                braking_time += 1

                # tezlik
                V = V - round(delta_capacity, 2)

        payload = {
            'braking_distance': round(S, 2),
            'braking_time': round(braking_time, 1),
            'result': result
        }

        return Response(payload, status=status.HTTP_200_OK)


class VagonDataList(generics.ListAPIView):
    queryset = TotalDataVagon.objects.all()
    serializer_class = TotalDataSerializer


class DeleteVagonsData(generics.DestroyAPIView):
    queryset = TotalDataVagon.objects.all()
    serializer_class = TotalDataSerializer

    def delete(self, request, *args, **kwargs):
        TotalDataVagon.objects.all().delete()
        TrainResistanceData.objects.all().delete()
        WeightModel.objects.all().delete()
        return Response({"success_message": "Muvaffaqiyatli o'chirildi!!!"})


class RailRoadSwitchList(generics.ListAPIView):
    serializer_class = RailRoadSwitchSerializer
    queryset = RailwaySwitchMark.objects.all()


class RailRoadCharacteristicLIstView(generics.ListAPIView):
    queryset = RailRoadCharacteristic.objects.all()
    serializer_class = RailRoadCharacteristicSerializer


class TrainRunningDistance(APIView):
    serializer_class = TrainRunningDistanceSerializer

    def post(self, request, *args, **kwargs):
        serializer = TrainRunningDistanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        weight = WeightModel.objects.last()
        locomotiv = weight.locomotiv
        vagon = VagonResistanceConstant.objects.first()
        P = weight.locomotiv_weight
        Q = weight.vagons_weight
        # Todo qanday topishni sorash kerak boladi
        a = (locomotiv.value_ao * P + vagon.value_ao * Q) / (P + Q)
        b = (locomotiv.value_bo * P + vagon.value_bo * Q) / (P + Q)
        c = (locomotiv.value_co * P + vagon.value_co * Q) / (P + Q)

        S = 0
        Vqb = 0
        i = 0
        tqo = 0

        Vl = 0
        Vl1 = 0

        # yoqilgi miqdori
        Yt_um = 0

        # kiritiladigan o'zgarmaslar
        Vmax = data['max_capacity']
        Kt1 = data['coefficient1']
        Kt2 = data['coefficient2']
        for item in data['values']:
            # F ustun: maksimal tezlik hisobi
            if float(Kt1) * float(item['declivity']) + float(Kt2) > Vmax:
                Vmax = Vmax
            else:
                Vmax = float(Kt1) * float(item['declivity']) + float(Kt2)

            # G ustun: Vl ni topish
            if Vqb % 5 < 2.5:
                Vl = Vqb - Vqb % 5
            else:
                Vl = Vqb + 5 - Vqb % 5

            # H ustun: Vl+1 ni topish
            if Vl < 90:
                Vl1 = Vl + 5
            else:
                Vl1 = Vl

            # I ustun:
            Fl = get_pulling_force(Vl)
            Fl1 = get_pulling_force(Vl1)

            # K ustun: Lokomotivning har bir qadamdagi ulanish kuchisiz tortish kuchi
            Flusi = ((Vqb - Vl) * (Fl + Fl1)) / (Vl - Vl1) + Fl

            # L ustun: lokomotivning har bir qadamdagi ulinish kuchiga egrilikning ta'sirini ifodalovchi koeffitsiyent
            if item['radius'] >= 800:
                Krfui = 800
            else:
                Krfui = (3.5 * item['radius']) / (400 + 3 * item['radius'])

            # M ustun: Lokomotivning har bir qadamdagi, egrilikning ta'sirini hiosbga oluvchi ulanish kuchi
            Flubi = 1000 * P * Krfui * (2.5 + 8 / (100 + 20 * float(Vqb)))

            # N ustun: lokomotivning har bir qadamdagi tortish kuchini topish
            if Flubi < Flusi:
                Ft = Flubi
            else:
                Ft = Flusi

            # O ustun: har bir qadamdagi harakatga manyovr tarkibining qarshiligi
            wi = a + b * Vqb + c * Vqb * Vqb

            # P ustun: har bir qadamdagi tezlikning o'zgarishi quyidagicha topiladi
            dV = math.sqrt(Vqb * Vqb + 0.24 * ((Flubi / (P + Q)) - wi - i) * float(item['distance'])) - Vqb

            # Q ustun: Ha rbir qadam oxiridagi tezlikning qiymati
            if Vqb + dV > Vmax:
                Vqo = Vmax
            else:
                Vqo = Vqb + dV

            # S ustun: har bir qadamdag vaqting o'zgarishi
            dt = 60 * float(item['distance']) / (500 * (float(Vqb) + float(Vqo)))

            # har bir qadam boshidagi tezlik oldingi qadam oxiridagi tezlikka teng boladi
            Vqb = float(Vqo)

            # yoqilgi hisobi
            Vavg = float((Vqb + Vqo) / 2)

            # tezlikka qarab ozgarmas yoqilgi miqdori
            if Vavg > 20:
                Ymiqdori = 203
            else:
                Ymiqdori = 11.5

            # yoqilgi miqdori
            Yt = float(Ymiqdori * dt / 60)

            Yt_um = Yt_um + Yt

            # T ustun: Har bir qadam oxirigidagi vaqtning qiymati
            tqo = tqo + dt

            S = S + item['distance']

        payload = {
            "dizel": round(Yt_um, 2),
            "distance": round(S, 2),
            "time": round(tqo*60, 1)
        }
        return Response(payload, status=status.HTTP_200_OK)




