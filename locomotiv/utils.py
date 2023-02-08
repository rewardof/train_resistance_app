import xlwt
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from xlwt import Alignment, Pattern
from django.http import HttpResponse

from locomotiv.models import TotalDataVagon, TrainResistanceData, VagonResistanceConstant, RailwaySwitchMark, \
    RailRoadCharacteristic
from locomotiv.wind_dict import get_wind_coefficient


def get_vagon_data(number, load_weight):
    number = str(number)
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

    if number_of_arrow == 0:
        number_of_arrow = 4
    total_weight = round(load_weight + netto_vagon, 2)
    bullet_weight = total_weight / number_of_arrow
    data = {
        "number_vagon": number,
        'load_weight': round(load_weight, 2),
        "number_of_arrow": number_of_arrow,
        "netto_vagon": netto_vagon,
        "total_weight": total_weight,
        "length_vagon": length_vagon,
        "bullet_weight": round(bullet_weight, 2)
    }
    return data


def resistance_export_excel(request):
    data = list(TrainResistanceData.objects.all())[-61:]
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="train_resistances.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Umumiy Qarshiliklar')
    row_num = 0

    alignment = Alignment()
    alignment.wrap = True
    alignment.horz = Alignment.HORZ_CENTER
    alignment.vert = Alignment.VERT_CENTER

    pattern = Pattern()
    pattern.pattern_back_color = 'blue'

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment = alignment
    font_style.pattern = pattern

    columns = ['Tezlik', 'Lokomotivning\n tortish rejimidagi \n harakatiga asosiy\nsolishtirma qarshilik',
               ' Lokomotivning salt yurish rejimidagi harakatiga asosiy solishtirma qarshilik',
               'Vagonlarning harakatiga asosiy solishtirma qarshilik',
               ' Manyovr tarkibining tortish rejimidagi harakatiga asosiy solishtirma qarshilik',
               'Manyovr tarkibining salt yurish rejimidagi harakatiga asosiy solishtirma qarshilik',
               "Nishablikning solishtirma qarshiligi",
               "Egrilikning solishtirma qarshilik", "Strelkali o’tkazgichlarning solishtirma qarshiligi",
               "Past haroratning solishtirma qarshiligi",
               "Harakatga qarama-qarshi va yon tomondan shamolning solishtirma qarshiligi",
               "Vagonlar bilan oldinda harakatlangandagi solishtirma qarshilik",
               "Yo’l holatining solishtirma qarshiligi",
               "Manoyvr tarkibining tortish rejimidagi harakatiga umumiy qarshilik",
               "Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik",
               "Manyovr tarkibining salt rejimidagi harakatiga umumiy qarshilik",
               "Manyovr tarkibining tortish rejimidagi harakatiga solishtirma qarshilik"]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, str(columns[col_num]), style=font_style)

    alignment = Alignment()
    alignment.wrap = True
    alignment.horz = Alignment.HORZ_CENTER
    font_style = xlwt.XFStyle()
    font_style.alignment = alignment
    ws.col(0).width = 2000
    ws.col(1).width = 5000
    ws.col(2).width = 8000
    ws.col(3).width = 8000
    ws.col(4).width = 8000
    ws.col(5).width = 8000

    ws.col(6).width = 8000
    ws.col(7).width = 8000
    ws.col(8).width = 8000
    ws.col(9).width = 8000
    ws.col(10).width = 8000
    ws.col(11).width = 8000
    ws.col(12).width = 8000
    ws.col(13).width = 8000
    ws.col(14).width = 8000
    ws.col(15).width = 8000
    ws.col(16).width = 8000

    for instance in data:
        row_num += 1
        ws.write(row_num, 0, instance.capacity, font_style)
        ws.write(row_num, 1, instance.locomotiv_traction_mode, font_style)
        ws.write(row_num, 2, instance.locomotiv_idle_mode, font_style)
        ws.write(row_num, 3, instance.total_resistance_vagon, font_style)
        ws.write(row_num, 4, instance.total_resistance_traction, font_style)
        ws.write(row_num, 5, instance.total_resistance_idle, font_style)

        ws.write(row_num, 6, instance.declivity_resistance, font_style)
        ws.write(row_num, 7, instance.curvature_resistance, font_style)
        ws.write(row_num, 8, instance.switch_curvature_resistance, font_style)
        ws.write(row_num, 9, instance.outside_temperature_resistance, font_style)
        ws.write(row_num, 10, instance.wind_capacity_resistance, font_style)
        ws.write(row_num, 11, instance.resistance_vagon_ahead, font_style)
        ws.write(row_num, 12, instance.railroad_condition_resistance, font_style)
        ws.write(row_num, 13, instance.all_traction_resistance, font_style)
        ws.write(row_num, 14, instance.specific_traction_resistance, font_style)
        ws.write(row_num, 15, instance.all_idle_resistance, font_style)
        ws.write(row_num, 16, instance.specific_idle_resistance, font_style)

    wb.save(response)
    return response


def vagon_data_excel(request):
    queryset = TotalDataVagon.objects.all()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="vagon.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Vagon Data')
    row_num = 0

    alignment = Alignment()
    alignment.wrap = True
    alignment.horz = Alignment.HORZ_CENTER
    alignment.vert = Alignment.VERT_CENTER

    pattern = Pattern()
    pattern.pattern_back_color = 'blue'

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.alignment = alignment
    font_style.pattern = pattern

    columns = ['№', 'Vagon raqami', "Yuk og'irligi", "Vagon og'irligi", "Vagon uzunligi", "O'qlar soni",
               "Umumiy og'irlik", "O'qqa tushadigan og'irlik"]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, str(columns[col_num]), style=font_style)

    alignment = Alignment()
    alignment.wrap = True
    alignment.horz = Alignment.HORZ_CENTER
    font_style = xlwt.XFStyle()
    font_style.alignment = alignment
    ws.col(0).width = 2000
    ws.col(1).width = 4000
    ws.col(2).width = 4000
    ws.col(3).width = 4000
    ws.col(4).width = 4000
    ws.col(5).width = 4000
    ws.col(6).width = 4000
    ws.col(7).width = 4000

    for instance in queryset:
        row_num += 1
        ws.write(row_num, 0, row_num, font_style)
        ws.write(row_num, 1, instance.number_vagon, font_style)
        ws.write(row_num, 2, instance.load_weight, font_style)
        ws.write(row_num, 3, instance.netto_vagon, font_style)
        ws.write(row_num, 4, instance.length_vagon, font_style)
        ws.write(row_num, 5, instance.number_of_arrow, font_style)
        ws.write(row_num, 6, instance.total_weight, font_style)
        ws.write(row_num, 7, instance.bullet_weight, font_style)
    wb.save(response)
    return response


def find_locomotiv_idle_mode(locomotiv, capacity):
    return 9.81 * (locomotiv.value_aox + locomotiv.value_box * capacity +
                   locomotiv.value_cox * capacity * capacity)


def find_total_resistance_vagon(queryset, capacity):
    cons_values = VagonResistanceConstant.objects.first()
    sum_resistance = 0
    sum_brutto_vagon = find_sum_brutto_vagon(queryset)
    for vagon in queryset:
        if vagon.bullet_weight > 6 and vagon.number_of_arrow == 4:
            vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ao + cons_values.value_bo * capacity +
                                                    cons_values.value_co * capacity * capacity) / vagon.bullet_weight,
                                                   2))

        elif vagon.number_of_arrow == 8:
            vagon_resistance = 9.81 * (0.7 + round((cons_values.value_ax + cons_values.value_bx * capacity +
                                                    cons_values.value_cx * capacity * capacity) / vagon.bullet_weight,
                                                   2))
        else:
            vagon_resistance = round(
                (9.81 * (cons_values.value_aox + cons_values.value_box * capacity +
                         cons_values.value_cox * capacity * capacity)), 2)

        sum_resistance += vagon_resistance * vagon.total_weight

    total_resistance_vagon = round(sum_resistance / sum_brutto_vagon, 2)

    return total_resistance_vagon


def find_sum_brutto_vagon(queryset):
    sum_brutto_vagon = 0
    for vagon in queryset:
        sum_brutto_vagon += vagon.total_weight
    return sum_brutto_vagon


def find_sum_length_vagons(queryset):
    sum_length_vagons = 0
    for vagon in queryset:
        sum_length_vagons += vagon.length_vagon
    return sum_length_vagons


def find_total_number_of_pads(queryset):
    total_number_of_pads = 0
    for vagon in queryset:
        total_number_of_pads += vagon.number_of_arrow
    return total_number_of_pads


def find_locomotiv_traction_mode(locomotiv, capacity):
    locomotiv_traction_mode = 9.81 * (locomotiv.value_ao + locomotiv.value_bo * capacity +
                                      locomotiv.value_co * capacity * capacity)
    return locomotiv_traction_mode


def find_locomotiv_idle_mode(locomotiv, capacity):
    locomotiv_idle_mode = 9.81 * (locomotiv.value_aox + locomotiv.value_box * capacity +
                                  locomotiv.value_cox * capacity * capacity)
    return locomotiv_idle_mode


def find_total_resistance_traction(locomotiv, capacity, vagons_queryset):
    total_resistance_traction = (find_locomotiv_traction_mode(locomotiv, capacity) * locomotiv.weigth
                                 + find_total_resistance_vagon(vagons_queryset, capacity) * find_sum_brutto_vagon(
                vagons_queryset)) / (
                                        locomotiv.weigth + find_sum_brutto_vagon(vagons_queryset))
    return total_resistance_traction


def find_total_resistance_idle(locomotiv, capacity, vagons_queryset):
    total_resistance_idle = (find_locomotiv_idle_mode(locomotiv, capacity) * locomotiv.weigth
                             + find_total_resistance_vagon(vagons_queryset, capacity) * find_sum_brutto_vagon(
                vagons_queryset)) / (
                                    locomotiv.weigth + find_sum_brutto_vagon(vagons_queryset))
    return total_resistance_idle


def find_declivity_resistance(declivity):
    return 9.81 * declivity


def find_curvature_resistance(radius, length_curvature, locomotiv, vagons_queryset):
    Lp = find_sum_length_vagons(vagons_queryset) + locomotiv.lenght
    if length_curvature == 0 or radius == 0:
        return 0
    else:
        if length_curvature < Lp:
            Wor = 9.81 * 700 * length_curvature / radius / Lp
        else:
            Wor = 9.81 * 700 / radius
        return Wor


def find_curvature_resistance_for_switch(railway_switch, locomotiv, vagons_queryset):
    print('sdas')
    if railway_switch == 0:
        return 0
    Lp = find_sum_length_vagons(vagons_queryset) + locomotiv.lenght
    try:
        railway_switch = RailwaySwitchMark.objects.get(id=railway_switch)
    except:
        raise ValidationError({"error_message": "Bunday id li strelkali o'tkazgich mavjud emas!!!"})

    if Lp > railway_switch.length_curvature:
        Wor_for_switch = 9.81 * 700 * railway_switch.length_curvature / railway_switch.radius / Lp
    else:
        Wor_for_switch = 9.81 * 700 / railway_switch.radius
    return Wor_for_switch


def find_outside_temperature_resistance(outside_temperature, locomotiv, capacity, vagons_queryset):
    if outside_temperature < -10:
        outside_temperature_resistance = 0.004 * find_total_resistance_traction(locomotiv, capacity,
                                                                                vagons_queryset)  # Wnt
    else:
        outside_temperature_resistance = 0
    return outside_temperature_resistance


def find_wind_capacity_resistance(wind_capacity, capacity, locomotiv, vagons_queryset):
    if wind_capacity <= 5:
        wind_capacity_resistance = 0
    else:
        if wind_capacity > 35:
            coef = get_wind_coefficient(capacity, 35)
        else:
            coef = get_wind_coefficient(capacity, int(wind_capacity))
        wind_capacity_resistance = coef * find_total_resistance_traction(locomotiv, capacity, vagons_queryset)
    return wind_capacity_resistance


def find_vagons_ahead_resistance(is_ahead, i, locomotiv, capacity, vagons_queryset):
    if is_ahead:
        Wvv = (0.15 + i / 1000) * find_total_resistance_traction(locomotiv, capacity, vagons_queryset)
    else:
        Wvv = 0
    return Wvv


def find_railroad_condition_resistance(railway_characteristics, locomotiv, capacity, vagons_queryset):
    try:
        railway_characteristics = RailRoadCharacteristic.objects.get(id=railway_characteristics)
    except:
        raise ValidationError({"error_message": "Bunday id li yo'l xarakteristikasi mavjud emas!!!"})
    railroad_condition_resistance = (railway_characteristics.coefficient - 1) * find_total_resistance_traction(
        locomotiv, capacity, vagons_queryset)
    return railroad_condition_resistance


def find_specific_idle_resistance(locomotiv, capacity, vagons_queryset, declivity, R, length_curvature,
                                  railway_switch, outside_temperature, wind_capacity, is_ahead,
                                  railway_characteristics):
    Ws = (find_locomotiv_idle_mode(locomotiv, capacity) * locomotiv.weigth + find_total_resistance_vagon(
        vagons_queryset, capacity) *
          find_sum_brutto_vagon(vagons_queryset))
    return Ws / (locomotiv.weigth + find_sum_brutto_vagon(vagons_queryset))


def get_pulling_force(capacity):
    dict = {
        0: 55000,
        5: 52000,
        10: 34500,
        15: 25500,
        20: 19500,
        25: 15500,
        30: 13500,
        35: 11500,
        40: 10000,
        45: 8750,
        50: 7500,
        60: 6000,
        70: 5000,
        80: 4000,
        90: 3000
    }
    return dict[capacity]

#      Ws = (locomotiv_idle_mode * locomotiv.weigth + total_resistance_vagon * sum_brutto_vagon + (
#                     locomotiv.weigth + sum_brutto_vagon) *
#                   (Wi + Wor + Wor_for_switch + outside_temperature_resistance +
#                    wind_capacity_resistance + Wvv + railroad_condition_resistance))


# + (locomotiv.weigth + find_sum_brutto_vagon(vagons_queryset)) *
#          (find_declivity_resistance(declivity) + find_curvature_resistance(R, length_curvature, locomotiv, vagons_queryset) +
#           find_curvature_resistance_for_switch(railway_switch, locomotiv, vagons_queryset) + find_outside_temperature_resistance(outside_temperature,
#                                                                                 locomotiv, capacity, vagons_queryset) +
#           find_wind_capacity_resistance(wind_capacity, capacity,
#                                         locomotiv, vagons_queryset) + find_vagons_ahead_resistance(is_ahead, declivity, locomotiv, capacity, vagons_queryset) +
#           find_railroad_condition_resistance(railway_characteristics,
#                                              locomotiv, capacity, vagons_queryset))
