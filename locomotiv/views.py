import math

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from locomotiv.models import Locomotiv, TotalDataVagon, VagonResistanceConstant, TrainResistanceData, RailwaySwitchMark, \
    RailRoadCharacteristic, WeightModel
from locomotiv.serializers import NumberSerializer, LocomotivSerializer, TotalDataSerializer, InputDataSerializer, \
    InputSerializer, RailRoadSwitchSerializer, RailRoadCharacteristicSerializer, TrainRunningDistanceSerializer
from locomotiv.utils import resistance_export_excel, find_total_resistance_vagon, find_total_number_of_pads, \
    find_sum_length_vagons, find_sum_brutto_vagon, find_locomotiv_traction_mode, find_locomotiv_idle_mode, \
    find_total_resistance_traction, find_total_resistance_idle, find_declivity_resistance, find_curvature_resistance, \
    find_curvature_resistance_for_switch, find_outside_temperature_resistance, find_wind_capacity_resistance, \
    find_vagons_ahead_resistance, find_railroad_condition_resistance, find_specific_idle_resistance, get_pulling_force
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
        load_weight = serializer.data['load_weight']
        first = int(number[:1])
        second = int(number[1:2])
        third = int(number[2:3])
        number_of_arrow = 0
        netto_vagon = 0
        length_vagon = 0
        if first == 2:
            if second == 0:
                number_of_arrow = 4
                netto_vagon = 24.2
                length_vagon = 15.35
            elif second in range(1, 4):
                number_of_arrow = 4
                netto_vagon = 23
                length_vagon = 14.73
            elif second in range(4, 6):
                number_of_arrow = 4
                netto_vagon = 24
                length_vagon = 14.73
            elif second in range(6, 8):
                number_of_arrow = 4
                netto_vagon = 26
                length_vagon = 15.35
            elif second == 8:
                number_of_arrow = 4
                netto_vagon = 27
                length_vagon = 17.64
            elif second == 9:
                number_of_arrow = 8
                netto_vagon = 29
                length_vagon = 18.8
        elif first == 3:
            if second == 0:
                if third in range(0, 5):
                    number_of_arrow = 4
                    netto_vagon = 25
                    length_vagon = 10
                elif third in range(5, 8):
                    number_of_arrow = 4
                    netto_vagon = 23
                    length_vagon = 10.87
                else:
                    number_of_arrow = 4
                    netto_vagon = 24
                    length_vagon = 11.42
            elif second == 1:
                if third in range(0, 5):
                    number_of_arrow = 4
                    netto_vagon = 25
                    length_vagon = 10
                else:
                    number_of_arrow = 4
                    netto_vagon = 23
                    length_vagon = 10.87
            elif second == 2:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 30.2
                    length_vagon = 11.52
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 23.2
                    length_vagon = 15.35
                else:
                    number_of_arrow = 4
                    netto_vagon = 23.2
                    length_vagon = 14.73
            elif second == 3:
                number_of_arrow = 4
                netto_vagon = 29
                length_vagon = 11.72
            elif second == 4 or 5:
                number_of_arrow = 4
                netto_vagon = 28
                length_vagon = 12.45
            elif second == 6:
                if third in range(5):
                    number_of_arrow = 6
                    netto_vagon = 40
                    length_vagon = 25.22
                elif third == 6:
                    number_of_arrow = 6
                    netto_vagon = 32
                    length_vagon = 16.4
                elif third == 7:
                    number_of_arrow = 6
                    netto_vagon = 85.5
                    length_vagon = 19.58
                elif third == 8:
                    number_of_arrow = 6
                    netto_vagon = 63.3
                    length_vagon = 24.82
                else:
                    number_of_arrow = 6
                    netto_vagon = 29
                    length_vagon = 15.22

            elif second == 7:
                if third in range(2):
                    number_of_arrow = 4
                    netto_vagon = 64.1
                    length_vagon = 18.22
                elif third == 2:
                    number_of_arrow = 4
                    netto_vagon = 70.7
                    length_vagon = 18.08
                elif third == 3:
                    number_of_arrow = 4
                    netto_vagon = 62.9
                    length_vagon = 18.8
                elif third == 4:
                    number_of_arrow = 4
                    netto_vagon = 69
                    length_vagon = 18.1
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 62.9
                    length_vagon = 18.16
                elif third == 6:
                    number_of_arrow = 4
                    netto_vagon = 87
                    length_vagon = 15.35
                else:
                    number_of_arrow = 4
                    netto_vagon = 59.5
                    length_vagon = 20.22
            else:
                number_of_arrow = 8
                netto_vagon = 85.5
                length_vagon = 22.45
        elif first == 4:
            if second == 0:
                number_of_arrow = 4
                netto_vagon = 22
                length_vagon = 14.91
            elif second in range(1, 9):
                number_of_arrow = 4
                netto_vagon = 20.9
                length_vagon = 14.62
            else:
                number_of_arrow = 8
                netto_vagon = 26.4
                length_vagon = 19.84
        elif first == 6:
            if second in range(8):
                number_of_arrow = 4
                netto_vagon = 24
                length_vagon = 14.41
            elif second == 8:
                number_of_arrow = 4
                netto_vagon = 22.6
                length_vagon = 14.41
            else:
                number_of_arrow = 8
                netto_vagon = 44.5
                length_vagon = 20.24
        elif first == 7:
            if second == 0:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 31.5
                    length_vagon = 14.06
                elif third in range(1, 4):
                    number_of_arrow = 4
                    netto_vagon = 36.5
                    length_vagon = 14.62
                elif third in range(4, 7):
                    number_of_arrow = 4
                    netto_vagon = 24.2
                    length_vagon = 12.02
                else:
                    number_of_arrow = 4
                    netto_vagon = 27.5
                    length_vagon = 12.02
            elif second == 1:
                number_of_arrow = 4
                netto_vagon = 24.5
                length_vagon = 12.22
            elif second == 2:
                number_of_arrow = 4
                netto_vagon = 24
                length_vagon = 12.2
            elif second in range(3, 5):
                if third in range(8):
                    number_of_arrow = 4
                    netto_vagon = 23.4
                    length_vagon = 12.49
                elif third == 8:
                    number_of_arrow = 4
                    netto_vagon = 28
                    length_vagon = 12.02
                else:
                    number_of_arrow = 4
                    netto_vagon = 28.5
                    length_vagon = 14.02
            elif second == 5:
                number_of_arrow = 4
                netto_vagon = 24.7
                length_vagon = 12.02
            elif second == 6:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 21.9
                    length_vagon = 12.02
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 20.4
                    length_vagon = 12.02
                elif third == 2:
                    number_of_arrow = 4
                    netto_vagon = 21.8
                    length_vagon = 12.02
                elif third == 3:
                    number_of_arrow = 4
                    netto_vagon = 23.5
                    length_vagon = 12.03
                elif third == 4:
                    number_of_arrow = 4
                    netto_vagon = 23.5
                    length_vagon = 12.03
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 35.3
                    length_vagon = 15.72
                else:
                    number_of_arrow = 4
                    netto_vagon = 21.9
                    length_vagon = 12.03
            elif second == 7 or 8:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 24.7
                    length_vagon = 12.02
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 26
                    length_vagon = 12.02
                elif third == 2:
                    number_of_arrow = 4
                    netto_vagon = 23.2
                    length_vagon = 12.02
                elif third == 3 or 4:
                    number_of_arrow = 4
                    netto_vagon = 28
                    length_vagon = 12.03
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 22.3
                    length_vagon = 15.72
                else:
                    number_of_arrow = 4
                    netto_vagon = 22.3
                    length_vagon = 15.72
            elif second == 9:
                if third == 0 or 1:
                    number_of_arrow = 8
                    netto_vagon = 51
                    length_vagon = 18.69
                elif third in range(2, 6):
                    number_of_arrow = 8
                    netto_vagon = 48.8
                    length_vagon = 21.12
                else:
                    number_of_arrow = 8
                    netto_vagon = 51
                    length_vagon = 21.25
        elif first == 8:
            if second == 0:
                number_of_arrow = 4
                netto_vagon = 33.5
                length_vagon = 22.08
            elif second == 1 or 2:
                if third in range(4):
                    number_of_arrow = 4
                    netto_vagon = 32.0
                    length_vagon = 14.73
                elif third in range(4, 7):
                    number_of_arrow = 4
                    netto_vagon = 37
                    length_vagon = 16.12
                else:
                    number_of_arrow = 4
                    netto_vagon = 43.6
                    length_vagon = 14.73
            elif second == 3:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 52
                    length_vagon = 20.08
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 44
                    length_vagon = 20.08
                else:
                    number_of_arrow = 4
                    netto_vagon = 46
                    length_vagon = 20.08
            elif second == 4:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 41
                    length_vagon = 18.22
                else:
                    number_of_arrow = 4
                    netto_vagon = 43
                    length_vagon = 18.22
            elif second == 5:
                number_of_arrow = 4
                netto_vagon = 39
                length_vagon = 22.08
            elif second in range(6, 9):
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 39
                    length_vagon = 18.22
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 50.5
                    length_vagon = 18.22
                elif third in range(2, 7):
                    number_of_arrow = 4
                    netto_vagon = 39
                    length_vagon = 22.08
                else:
                    number_of_arrow = 4
                    netto_vagon = 43
                    length_vagon = 22.07
            else:
                number_of_arrow = 8
                netto_vagon = 67.7
                length_vagon = 24.73
        elif first == 9:
            if second == 0:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 26.5
                    length_vagon = 11.63
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 26.5
                    length_vagon = 11.72
                elif third == 2:
                    number_of_arrow = 4
                    netto_vagon = 20.5
                    length_vagon = 12.00
                elif third in range(3, 7):
                    number_of_arrow = 4
                    netto_vagon = 22.0
                    length_vagon = 14.72
                elif third == 7:
                    number_of_arrow = 4
                    netto_vagon = 26.0
                    length_vagon = 15.35
                elif third == 8:
                    number_of_arrow = 4
                    netto_vagon = 37.0
                    length_vagon = 22.16
                else:
                    number_of_arrow = 4
                    netto_vagon = 23.2
                    length_vagon = 12.00
            elif second == 1:
                if third in range(2):
                    number_of_arrow = 4
                    netto_vagon = 24.0
                    length_vagon = 10.00
                elif third in range(2, 5):
                    number_of_arrow = 4
                    netto_vagon = 23.0
                    length_vagon = 12.00
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 33.5
                    length_vagon = 25.84
                elif third == 6 or 7:
                    number_of_arrow = 4
                    netto_vagon = 30.00
                    length_vagon = 20.96
                else:
                    number_of_arrow = 4
                    netto_vagon = 37.00
                    length_vagon = 22.16
            elif second == 2:
                if third in range(4):
                    number_of_arrow = 4
                    netto_vagon = 23.2
                    length_vagon = 15.35
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 42.00
                    length_vagon = 24.54
                elif third == 6:
                    number_of_arrow = 4
                    netto_vagon = 25.00
                    length_vagon = 14.62
                elif third == 7:
                    number_of_arrow = 4
                    netto_vagon = 42.00
                    length_vagon = 24.54
                elif third == 8:
                    number_of_arrow = 4
                    netto_vagon = 34.00
                    length_vagon = 21.66
                else:
                    number_of_arrow = 4
                    netto_vagon = 24.6
                    length_vagon = 12.02
            elif second == 3:
                if third in range(7):
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 12.12
                else:
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 12.12
            elif second == 4:
                if third == 0 or 1:
                    number_of_arrow = 4
                    netto_vagon = 26.00
                    length_vagon = 25.22
                elif third in range(2, 5):
                    number_of_arrow = 4
                    netto_vagon = 21.00
                    length_vagon = 14.62
                elif third in range(5, 9):
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 19.62
                else:
                    number_of_arrow = 4
                    netto_vagon = 24.2
                    length_vagon = 25.62
            elif second == 5:
                number_of_arrow = 4
                netto_vagon = 20.4
                length_vagon = 14.62
            elif second == 6:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 14.72
                elif third == 1:
                    number_of_arrow = 4
                    netto_vagon = 45.00
                    length_vagon = 22.08
                elif third == 2:
                    number_of_arrow = 4
                    netto_vagon = 32.8
                    length_vagon = 24.73
                elif third == 3:
                    number_of_arrow = 4
                    netto_vagon = 28.00
                    length_vagon = 22.52
                elif third == 4:
                    number_of_arrow = 4
                    netto_vagon = 25.4
                    length_vagon = 14.73
                elif third == 5:
                    number_of_arrow = 4
                    netto_vagon = 25.6
                    length_vagon = 18.08
                elif third == 6:
                    number_of_arrow = 4
                    netto_vagon = 30.00
                    length_vagon = 14.62
                elif third == 7:
                    number_of_arrow = 4
                    netto_vagon = 33.8
                    length_vagon = 17.48
                elif third == 8:
                    number_of_arrow = 4
                    netto_vagon = 25.5
                    length_vagon = 12.02
                else:
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 12.02
            elif second == 7:
                if third == 0:
                    number_of_arrow = 4
                    netto_vagon = 31.3
                    length_vagon = 15.72
                elif third in range(1, 8):
                    number_of_arrow = 4
                    netto_vagon = 22.00
                    length_vagon = 19.22
                else:
                    number_of_arrow = 4
                    netto_vagon = 25.00
                    length_vagon = 12.22
            elif second == 8:
                number_of_arrow = 4
                netto_vagon = 25.00
                length_vagon = 12.22
            else:
                number_of_arrow = 8
                netto_vagon = 54.4
                length_vagon = 23.4
        else:
            return Response({"error_message": "Vagon raqami 0 yoki 1 bilan boshlanmasligi kerak"},
                            status=status.HTTP_400_BAD_REQUEST)
        input_data = {
            'number_of_arrow': number_of_arrow,
            'netto_vagon': netto_vagon,
            'length_vagon': length_vagon
        }
        input_serializer = InputDataSerializer(data=input_data)
        input_serializer.is_valid(raise_exception=True)
        total_weight = round(load_weight + input_serializer.validated_data['netto_vagon'], 2)
        bullet_weight = total_weight / input_serializer.validated_data['number_of_arrow']
        data = {
            "number_vagon": number,
            'load_weight': round(load_weight, 2),
            "number_of_arrow": input_serializer.validated_data['number_of_arrow'],
            "netto_vagon": input_serializer.validated_data['netto_vagon'],
            "total_weight": total_weight,
            "length_vagon": input_serializer.validated_data['length_vagon'],
            "bullet_weight": round(bullet_weight, 2)
        }
        serializer = TotalDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data, status=status.HTTP_200_OK)


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
        # kiritiladigan o'zgarmaslar
        Vmax = data['max_capacity']
        Kt1 = data['coefficient1']
        Kt2 = data['coefficient2']
        for item in data['values']:
            # F ustun: maksimla tezlik hisobi
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
            Flubi = 1000 * P * Krfui * (2.5 + 8 / (100 + 20 * Vqb))

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
            Vqb = Vqo

            # T ustun: Har bir qadam oxirigidagi vaqtning qiymati
            tqo = tqo + dt

            S = S + item['distance']

        payload = {
            "distance": S,
            "time": tqo
        }
        return Response(payload, status=status.HTTP_200_OK)




