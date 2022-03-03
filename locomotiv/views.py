from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from locomotiv.models import Locomotiv, TotalDataVagon, VagonResistanceConstant, TrainResistanceData, RailwaySwitchMark, \
    RailRoadCharacteristic
from locomotiv.serializers import NumberSerializer, LocomotivSerializer, TotalDataSerializer, InputDataSerializer, \
    InputSerializer, RailRoadSwitchSerializer, RailRoadCharacteristicSerializer
from locomotiv.utils import resistance_export_excel
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
            return Response({"error_message": "Vagon raqami 0 yoki 1 bilan boshlanmasligi kerak"}, status=status.HTTP_400_BAD_REQUEST)
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


class CalculateResultView(generics.ListCreateAPIView):
    queryset = Locomotiv.objects.filter(is_active=True)
    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        try:
            locomotiv = Locomotiv.objects.get(id=self.kwargs['locomotiv_id'])
        except:
            return Response({"error_message": "Bu idli lokomotiv mavjud emas!!!"}, status=status.HTTP_400_BAD_REQUEST)
        result = []
        for capacity in range(61):

            locomotiv_traction_mode = 9.81 * (locomotiv.value_ao + locomotiv.value_bo * capacity +
                                              locomotiv.value_co * capacity * capacity)
            locomotiv_idle_mode = 9.81 * (locomotiv.value_aox + locomotiv.value_box * capacity +
                                          locomotiv.value_cox * capacity * capacity)

            # vagons data
            cons_values = VagonResistanceConstant.objects.first()

            sum_resistance = 0
            sum_brutto_vagon = 0
            for vagon in TotalDataVagon.objects.all():
                if vagon.bullet_weight > 6 and vagon.number_of_arrow == 4:
                    vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ao + cons_values.value_bo * capacity +
                                                            cons_values.value_co * capacity * capacity) / vagon.bullet_weight,
                                                           2))

                elif vagon.number_of_arrow == 8:
                    print('sakkiz')
                    vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ax + cons_values.value_bx * capacity +
                                                            cons_values.value_cx * capacity * capacity) / vagon.bullet_weight,
                                                           2))
                else:
                    vagon_resistance = round(
                        (9.81 * (cons_values.value_aox + cons_values.value_box * capacity +
                                 cons_values.value_cox * capacity * capacity)), 2)
                sum_resistance += vagon_resistance * vagon.total_weight
                sum_brutto_vagon += vagon.total_weight

            total_resistance_vagon = round(sum_resistance / sum_brutto_vagon, 2)

            total_resistance_traction = (locomotiv_traction_mode * locomotiv.weigth
                                         + total_resistance_vagon * sum_brutto_vagon) / (
                                                locomotiv.weigth + sum_brutto_vagon)
            total_resistance_idle = (locomotiv_idle_mode * locomotiv.weigth
                                     + total_resistance_vagon * sum_brutto_vagon) / (
                                            locomotiv.weigth + sum_brutto_vagon)

            # additional resistances

            # Nishablikning solishtirma
            i = request.data.get('declivity')
            Wi = 9.81 * i

            # Egrilikning solishtirma qarshilik
            Lp = sum_length_vagons + locomotiv.lenght
            R = request.data.get('radius')
            length_curvature = request.data.get('length_curvature')
            if length_curvature < Lp:
                Wor = 9.81 * 700 * length_curvature / R / Lp
            else:
                Wor = 9.81 * 700 / R

            # Strelkali o’tkazgichlarning solishtirma qarshiligi
            railway_switch = request.data.get('railway_switch_mark')
            try:
                railway_switch = RailwaySwitchMark.objects.get(id=railway_switch)
            except:
                return Response({"error_message": "Bunday id li strelkali o'tkazgich mavjud emas!!!"}, status=status.HTTP_404_NOT_FOUND)
            if Lp > railway_switch.length_curvature:
                Wor_for_switch = 9.81 * 700 * railway_switch.length_curvature / railway_switch.radius / Lp
            else:
                Wor_for_switch = 9.81 * 700 / railway_switch.radius

            # Past haroratning solishtirma qarshiligi
            outside_temperature = request.data.get('outside_temperature')
            if outside_temperature < -10:
                outside_temperature_resistance = 0.004 * total_resistance_traction # Wnt
            else:
                outside_temperature_resistance = 0

            # Harakatga qarama qarshi va yon tomondan shamolning solishtirma qarshiligi
            wind_capacity = request.data.get('wind_capacity')
            if wind_capacity < 5:
                wind_capacity_resistance = 0
            else:
                if wind_capacity > 35:
                    coef = get_wind_coefficient(capacity, 35)
                else:
                    coef = get_wind_coefficient(capacity, int(wind_capacity))
                wind_capacity_resistance = coef * total_resistance_traction

            # Vagonlar bilan oldinda harakatlangandagi solishtirma qarshilik

            is_ahead = request.data.get('is_ahead')
            if is_ahead:
                Wvv = (0.15 + i/1000) * total_resistance_traction
                print(Wvv)
            else:
                Wvv = 0

            #  Yo’l holatining solishtirma qarshiligi

            railway_characteristics = request.data.get('railway_characteristic')
            try:
                railway_characteristics = RailRoadCharacteristic.objects.get(id=railway_characteristics)
            except:
                return Response({"error_message": "Bunday id li yo'l xarakteristikasi mavjud emas!!!"}, status=status.HTTP_404_NOT_FOUND)
            railroad_condition_resistance = (railway_characteristics.coefficient - 1) * total_resistance_traction

            # Manoyvr tarkibining tortish rejimidagi harakatiga umumiy qarshilik.
            W = (locomotiv_traction_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (locomotiv.weigth + sum_brutto_vagon) *
                 (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
                  wind_capacity_resistance + Wvv + railroad_condition_resistance))

            # Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
            specific_traction_resistance = W / (locomotiv.weigth + sum_brutto_vagon)

            # Manyovr tarkibining salt rejimidagi harakatiga umumiy qarshilik
            Ws = (locomotiv_idle_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
                        locomotiv.weigth + sum_brutto_vagon) *
                 (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
                  wind_capacity_resistance + Wvv + railroad_condition_resistance))

            # Manyovr tarkibining Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
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
        return Response(result, status=status.HTTP_200_OK)


class VagonDataList(generics.ListAPIView):
    queryset = TotalDataVagon.objects.all()
    serializer_class = TotalDataSerializer


class DeleteVagonsData(generics.DestroyAPIView):
    queryset = TotalDataVagon.objects.all()
    serializer_class = TotalDataSerializer

    def delete(self, request, *args, **kwargs):
        TotalDataVagon.objects.all().delete()
        TrainResistanceData.objects.all().delete()
        return Response({"success_message": "Muvaffaqiyatli o'chirildi!!!"})


class RailRoadSwitchList(generics.ListAPIView):
    serializer_class = RailRoadSwitchSerializer
    queryset = RailwaySwitchMark.objects.all()


class RailRoadCharacteristicLIstView(generics.ListAPIView):
    queryset = RailRoadCharacteristic.objects.all()
    serializer_class = RailRoadCharacteristicSerializer