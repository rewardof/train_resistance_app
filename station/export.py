import xlwt
from django.http import HttpResponse
from xlwt import Alignment, Pattern


def export_natural_list_data(queryset):
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

    columns = [
        '№',
        'Vagon raqami',
        'Boradigan stansiya',
        "Saralanadigan yo'l"
    ]

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
    for instance in queryset:
        row_num += 1
        ws.write(row_num, 0, instance.order, font_style)
        ws.write(row_num, 1, instance.number_vagon, font_style)
        ws.write(row_num, 2, instance.destination_station, font_style)
        ws.write(row_num, 3, instance.road_number.number if instance.road_number else "", font_style)
    wb.save(response)
    return response