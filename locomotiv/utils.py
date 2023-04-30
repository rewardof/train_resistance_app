import xlwt
from xlwt import Alignment, Pattern
from django.http import HttpResponse

from locomotiv.models import TotalDataVagon
from utils.constants import CONSTANTS


def get_vagon_data(number, load_weight):
    number = str(number)
    first = int(number[:1])
    second = int(number[1:2])
    third = int(number[2:3])
    number_of_arrow = 0
    netto_vagon = 0
    length_vagon = 0
    if first == 2:
        vagon_type = CONSTANTS.VAGON_TYPE.KR
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
            number_of_arrow = 4
            netto_vagon = 29
            length_vagon = 18.8
    elif first == 3:
        vagon_type = CONSTANTS.VAGON_TYPE.PR
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
        vagon_type = CONSTANTS.VAGON_TYPE.PL
        if second == 0:
            number_of_arrow = 4
            netto_vagon = 22
            length_vagon = 14.91
        elif second in range(1, 9):
            number_of_arrow = 4
            netto_vagon = 20.9
            length_vagon = 14.62
        else:
            number_of_arrow = 4
            netto_vagon = 26.4
            length_vagon = 19.84
    elif first == 5:
        if second in range(2):
            number_of_arrow = 4
            netto_vagon = 24.2
            length_vagon = 14.41
            vagon_type = CONSTANTS.VAGON_TYPE.SYS
        elif second == 2:
            number_of_arrow = 4
            netto_vagon = 24
            length_vagon = 14.73
            vagon_type = CONSTANTS.VAGON_TYPE.KR

        elif second == 3:
            number_of_arrow = 4
            netto_vagon = 22
            length_vagon = 14.72
            vagon_type = CONSTANTS.VAGON_TYPE.XP

        elif second == 4:
            number_of_arrow = 4
            netto_vagon = 22
            length_vagon = 14.91
            vagon_type = CONSTANTS.VAGON_TYPE.PL

        elif second == 5:
            number_of_arrow = 4
            netto_vagon = 22
            length_vagon = 14.72
            vagon_type = CONSTANTS.VAGON_TYPE.PR

        elif second == 6:
            number_of_arrow = 4
            netto_vagon = 24
            length_vagon = 14.41
            vagon_type = CONSTANTS.VAGON_TYPE.PV

        elif second == 7:
            number_of_arrow = 4
            netto_vagon = 24.2
            length_vagon = 14.02
            vagon_type = CONSTANTS.VAGON_TYPE.SYS

        elif second == 8:
            number_of_arrow = 4
            netto_vagon = 32
            length_vagon = 14.73
            vagon_type = CONSTANTS.VAGON_TYPE.RF

        elif second == 9:
            number_of_arrow = 4
            netto_vagon = 26
            length_vagon = 15.35
            vagon_type = CONSTANTS.VAGON_TYPE.PR
    elif first == 6:
        vagon_type = CONSTANTS.VAGON_TYPE.PV
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
        vagon_type = CONSTANTS.VAGON_TYPE.SYS
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
        vagon_type = CONSTANTS.VAGON_TYPE.RF
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
        vagon_type = CONSTANTS.VAGON_TYPE.PR
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
            vagon_type = CONSTANTS.VAGON_TYPE.XP
            if third in range(7):
                number_of_arrow = 4
                netto_vagon = 22.00
                length_vagon = 12.12
            else:
                number_of_arrow = 4
                netto_vagon = 22.00
                length_vagon = 12.12
        elif second == 4:
            vagon_type = CONSTANTS.VAGON_TYPE.PL
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
            vagon_type = CONSTANTS.VAGON_TYPE.XP
            number_of_arrow = 4
            netto_vagon = 20.4
            length_vagon = 14.62
        elif second == 6:
            vagon_type = CONSTANTS.VAGON_TYPE.SYS
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
                vagon_type = CONSTANTS.VAGON_TYPE.XP
                number_of_arrow = 4
                netto_vagon = 25.6
                length_vagon = 18.08
            elif third == 6:
                vagon_type = CONSTANTS.VAGON_TYPE.XP
                number_of_arrow = 4
                netto_vagon = 30.00
                length_vagon = 14.62
            elif third == 7:
                vagon_type = CONSTANTS.VAGON_TYPE.XP
                number_of_arrow = 4
                netto_vagon = 33.8
                length_vagon = 17.48
            elif third == 8:
                vagon_type = CONSTANTS.VAGON_TYPE.XP
                number_of_arrow = 4
                netto_vagon = 25.5
                length_vagon = 12.02
            else:
                vagon_type = CONSTANTS.VAGON_TYPE.XP
                number_of_arrow = 4
                netto_vagon = 22.00
                length_vagon = 12.02
        elif second == 7:
            vagon_type = CONSTANTS.VAGON_TYPE.XP
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
            vagon_type = CONSTANTS.VAGON_TYPE.XP
            number_of_arrow = 4
            netto_vagon = 25.00
            length_vagon = 12.22
        else:
            vagon_type = CONSTANTS.VAGON_TYPE.XP
            number_of_arrow = 8
            netto_vagon = 54.4
            length_vagon = 23.4

    if number_of_arrow == 0:
        number_of_arrow = 4
    total_weight = round(load_weight + netto_vagon, 2)
    bullet_weight = total_weight / number_of_arrow
    data = {
        "number_vagon": number,
        'vagon_type': vagon_type,
        'load_weight': round(load_weight, 2),
        "number_of_arrow": number_of_arrow,
        "netto_vagon": netto_vagon,
        "total_weight": total_weight,
        "length_vagon": length_vagon,
        "bullet_weight": round(bullet_weight, 2)
    }
    return data


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

    columns = ['№', 'Vagon raqami', "Vagon turi", "Yuk og'irligi", "Vagon og'irligi", "Vagon uzunligi", "O'qlar soni",
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
    ws.col(8).width = 4000

    for instance in queryset:
        row_num += 1
        ws.write(row_num, 0, row_num, font_style)
        ws.write(row_num, 1, instance.number_vagon, font_style)
        ws.write(row_num, 2, instance.vagon_type, font_style)
        ws.write(row_num, 3, instance.load_weight, font_style)
        ws.write(row_num, 4, instance.netto_vagon, font_style)
        ws.write(row_num, 5, instance.length_vagon, font_style)
        ws.write(row_num, 6, instance.number_of_arrow, font_style)
        ws.write(row_num, 7, instance.total_weight, font_style)
        ws.write(row_num, 8, instance.bullet_weight, font_style)
    wb.save(response)
    return response


def is_true(value):
    if value in ['true', 'True', 'TRUE', '1', 1, True]:
        return True
    elif value in ['false', 'False', 'FALSE', '0', 0, False]:
        return False
