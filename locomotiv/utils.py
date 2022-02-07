import random
from io import BytesIO

import xlwt
from xlwt import Alignment, Pattern, Borders
from django.core.files import File
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.utils import timezone

from locomotiv.models import Excel, TotalDataVagon


def resistance_export_excel(data):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="something.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('User')
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

    columns = ['Tezlik', 'Lokomotivning\n tortish rejimidagi \n harakatiga asosiy\nsolishtirma qarshilik', ' Lokomotivning salt yurish rejimidagi harakatiga asosiy solishtirma qarshilik',
               'Vagonlarning harakatiga asosiy solishtirma qarshilik', ' Manyovr tarkibining tortish rejimidagi harakatiga asosiy solishtirma qarshilik',
               'Manyovr tarkibining salt yurish rejimidagi harakatiga asosiy solishtirma qarshilik']

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

    for instance in data:
        row_num += 1
        ws.write(row_num, 0, instance["capacity"], font_style)
        ws.write(row_num, 1, instance['locomotiv_traction_mode'], font_style)
        ws.write(row_num, 2, instance['locomotiv_idle_mode'], font_style)
        ws.write(row_num, 3, instance['total_resistance_vagon'], font_style)
        ws.write(row_num, 4, instance['total_resistance_traction'], font_style)
        ws.write(row_num, 5, instance['total_resistance_idle'], font_style)
    number = random.randint(100000, 999999)
    wb.save(f'media/files/{number}.xls')
    instance = Excel.objects.create(file=f'files/{number}.xls')
    return instance


def export_excel(self, request, queryset):
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s%s.xls' % (
        'users-', timezone.now().strftime("%d-%m-%Y"))
    wb = resistance_export_excel(queryset)
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

    columns = ['№', 'Vagon raqami', "Vagon og'irligi", "Vagon uzunligi", "O'qlar soni", "Umumiy og'irlik", "O'qqa tushadigan og'irlik"]

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

    for instance in queryset:
        row_num += 1
        ws.write(row_num, 0, row_num, font_style)
        ws.write(row_num, 1, instance.number_vagon, font_style)
        ws.write(row_num, 2, instance.netto_vagon, font_style)
        ws.write(row_num, 3, instance.length_vagon, font_style)
        ws.write(row_num, 4, instance.number_of_arrow, font_style)
        ws.write(row_num, 5, instance.total_weight, font_style)
        ws.write(row_num, 6, instance.bullet_weight, font_style)
    wb.save(response)
    return response
