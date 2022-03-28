# class CalculateResultView(APIView):
#     queryset = Locomotiv.objects.filter(is_active=True)
#
#     # serializer_class = InputSerializer
#
#     def post(self, request, *args, **kwargs):
#         global Kt
#         locomotiv_id = self.request.data.get('id')
#         try:
#             locomotiv = Locomotiv.objects.get(id=locomotiv_id)
#         except:
#             return Response({"error_message": "Bu idli lokomotiv mavjud emas!!!"}, status=status.HTTP_400_BAD_REQUEST)
#         result = []
#         for capacity in range(61):
#
#             locomotiv_traction_mode = 9.81 * (locomotiv.value_ao + locomotiv.value_bo * capacity +
#                                               locomotiv.value_co * capacity * capacity)
#             locomotiv_idle_mode = 9.81 * (locomotiv.value_aox + locomotiv.value_box * capacity +
#                                           locomotiv.value_cox * capacity * capacity)
#             sum_resistance = 0
#             sum_brutto_vagon = 0
#             sum_length_vagons = 0
#             total_number_of_pads = find_total_number_of_pads()
#             for vagon in TotalDataVagon.objects.all():
#                 if vagon.bullet_weight > 6 and vagon.number_of_arrow == 4:
#                     vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ao + cons_values.value_bo * capacity +
#                                                             cons_values.value_co * capacity * capacity) / vagon.bullet_weight,
#                                                            2))
#
#                 elif vagon.number_of_arrow == 8:
#                     print('sakkiz')
#                     vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ax + cons_values.value_bx * capacity +
#                                                             cons_values.value_cx * capacity * capacity) / vagon.bullet_weight,
#                                                            2))
#                 else:
#                     vagon_resistance = round(
#                         (9.81 * (cons_values.value_aox + cons_values.value_box * capacity +
#                                  cons_values.value_cox * capacity * capacity)), 2)
#                 sum_resistance += vagon_resistance * vagon.total_weight
#                 sum_brutto_vagon += vagon.total_weight
#                 sum_length_vagons += vagon.length_vagon
#                 total_number_of_pads += vagon.number_of_arrow
#
#             vagons_queryset = TotalDataVagon.objects.all()
#
#             total_resistance_vagon = round(find_total_resistance_vagon(vagons_queryset, capacity))
#
#             total_resistance_traction = (locomotiv_traction_mode * locomotiv.weigth
#                                          + total_resistance_vagon * sum_brutto_vagon) / (
#                                                 locomotiv.weigth + sum_brutto_vagon)
#             total_resistance_idle = (locomotiv_idle_mode * locomotiv.weigth
#                                      + total_resistance_vagon * sum_brutto_vagon) / (
#                                             locomotiv.weigth + sum_brutto_vagon)
#
#             # additional resistances
#
#             # Nishablikning solishtirma
#             i = float(request.data.get('declivity'))
#             Wi = 9.81 * i
#
#             # Egrilikning solishtirma qarshilik
#             Lp = sum_length_vagons + locomotiv.lenght
#             R = float(request.data.get('radius'))
#             length_curvature = float(request.data.get('length_curvature'))
#             if length_curvature < Lp:
#                 Wor = 9.81 * 700 * length_curvature / R / Lp
#             else:
#                 Wor = 9.81 * 700 / R
#
#             # Strelkali o’tkazgichlarning solishtirma qarshiligi
#             railway_switch = int(request.data.get('railway_switch_mark'))
#             try:
#                 railway_switch = RailwaySwitchMark.objects.get(id=railway_switch)
#             except:
#                 return Response({"error_message": "Bunday id li strelkali o'tkazgich mavjud emas!!!"},
#                                 status=status.HTTP_404_NOT_FOUND)
#             if Lp > railway_switch.length_curvature:
#                 Wor_for_switch = 9.81 * 700 * railway_switch.length_curvature / railway_switch.radius / Lp
#             else:
#                 Wor_for_switch = 9.81 * 700 / railway_switch.radius
#
#             # Past haroratning solishtirma qarshiligi
#             outside_temperature = float(request.data.get('outside_temperature'))
#             if outside_temperature < -10:
#                 outside_temperature_resistance = 0.004 * total_resistance_traction  # Wnt
#             else:
#                 outside_temperature_resistance = 0
#
#             # Harakatga qarama qarshi va yon tomondan shamolning solishtirma qarshiligi
#             wind_capacity = float(request.data.get('wind_capacity'))
#             if wind_capacity < 5:
#                 wind_capacity_resistance = 0
#             else:
#                 if wind_capacity > 35:
#                     coef = get_wind_coefficient(capacity, 35)
#                 else:
#                     coef = get_wind_coefficient(capacity, int(wind_capacity))
#                 wind_capacity_resistance = coef * total_resistance_traction
#
#             # Vagonlar bilan oldinda harakatlangandagi solishtirma qarshilik
#
#             is_ahead = request.data.get('is_ahead')
#             if is_ahead:
#                 Wvv = (0.15 + i / 1000) * total_resistance_traction
#                 print(Wvv)
#             else:
#                 Wvv = 0
#
#             #  Yo’l holatining solishtirma qarshiligi
#
#             railway_characteristics = int(request.data.get('railway_characteristic'))
#             try:
#                 railway_characteristics = RailRoadCharacteristic.objects.get(id=railway_characteristics)
#             except:
#                 return Response({"error_message": "Bunday id li yo'l xarakteristikasi mavjud emas!!!"},
#                                 status=status.HTTP_404_NOT_FOUND)
#             railroad_condition_resistance = (railway_characteristics.coefficient - 1) * total_resistance_traction
#
#             # Manoyvr tarkibining tortish rejimidagi harakatiga umumiy qarshilik.
#             W = (locomotiv_traction_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
#                     locomotiv.weigth + sum_brutto_vagon) *
#                  (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
#                   wind_capacity_resistance + Wvv + railroad_condition_resistance))
#
#             # Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
#             specific_traction_resistance = W / (locomotiv.weigth + sum_brutto_vagon)
#
#             # Manyovr tarkibining salt rejimidagi harakatiga umumiy qarshilik
#             Ws = (locomotiv_idle_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
#                     locomotiv.weigth + sum_brutto_vagon) *
#                   (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
#                    wind_capacity_resistance + Wvv + railroad_condition_resistance))
#
#             # Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik
#             specific_idle_resistance = Ws / (locomotiv.weigth + sum_brutto_vagon)
#
#             is_magistral = request.data.get('is_magistral')
#
#             # Lokomotivni bitta tormoz kolodkasinining o‘qga bosilishidagi haqiqiy kuchi
#             total_lenght = locomotiv.lenght + sum_length_vagons
#
#             #  Lokomotivni bitta tormoz kolodkasinining o‘qga bosilishidagi haqiqiy kuchi
#             K = 2300 * 2 * total_number_of_pads
#
#             # tarkib umumiy og'irligi
#             total_weight = locomotiv.weigth + sum_brutto_vagon
#
#             braking_time = 0
#             if is_magistral:
#                 if total_lenght <= 500:
#                     if braking_time < 27:
#                         Kt = -0.0000191 * pow(braking_time, 3) - 0.000343 * pow(braking_time, 2) + 0.06 * braking_time
#                     else:
#                         Kt = 1
#                 elif total_lenght > 500:
#                     if braking_time < 33:
#                         Kt = -0.0000255 * pow(braking_time, 3) - 0.000766 * pow(braking_time, 2) + 0.033 * braking_time
#                     else:
#                         Kt = 1  # Todo shu yerda barcha sanoat tarkibi uchun degan joyi qolib turadi
#             else:
#                 if braking_time < 31:
#                     Kt = -0.0000107 * pow(braking_time, 3) - 0.00173 * pow(braking_time, 2) + 0.076 * braking_time
#                 else:
#                     Kt = 1
#
#             # G'ildirakka tormoz kolodkasi ishqalanishning haqiqiy iqtisodiy koeffitsienti
#
#             K0 = locomotiv.force_all_arrows * Kt
#
#             V = capacity
#             p1 = Kt * V
#
#             S = 0.6 * (0.016 * K0 + 100) / (0.08 * K0 + 100) * (V + 100) / (5 * V + 100) * K0
#
#             p0 = 0.6 * (0.016 * K0 + 100) / (0.08 * K0 + 100) * (V + 100) / (5 * V + 100)
#
#             p1 = 0.6 * (0.016 * K + 100) / (0.08 * K + 100) * (V + 100) / (5 * V + 100)
#
#             Vmt = K0 * p0 + K * p1
#
#             while V > 0:
#                 r = i + total_resistance_idle / 9.81 + Vmt / total_weight
#                 delta_v = r / 30
#                 avg_capacity = capacity - delta_v / 2
#                 S += avg_capacity / 3.6
#
#             data = {
#                 'capacity': capacity,
#                 "locomotiv_traction_mode": round(locomotiv_traction_mode, 2),
#                 'locomotiv_idle_mode': round(locomotiv_idle_mode, 2),
#                 'total_resistance_vagon': round(total_resistance_vagon, 2),
#                 'total_resistance_traction': round(total_resistance_traction, 2),
#                 'total_resistance_idle': round(total_resistance_idle, 2),
#
#                 'declivity_resistance': round(Wi, 2),
#                 'curvature_resistance': round(Wor, 2),
#                 'switch_curvature_resistance': round(Wor_for_switch, 2),
#                 'outside_temperature_resistance': round(outside_temperature_resistance, 2),
#                 'wind_capacity_resistance': round(wind_capacity_resistance, 2),
#                 'resistance_vagon_ahead': round(Wvv, 2),
#                 'railroad_condition_resistance': round(railroad_condition_resistance, 2),
#                 'all_traction_resistance': round(W, 2),
#                 'specific_traction_resistance': round(specific_traction_resistance, 2),
#                 'all_idle_resistance': round(Ws, 2),
#                 'specific_idle_resistance': round(specific_idle_resistance, 2)
#             }
#             TrainResistanceData.objects.create(**data)
#             result.append(data)
#         return Response(result, status=status.HTTP_200_OK)