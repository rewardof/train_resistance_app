from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from .models import Locomotiv, VagonResistanceConstant, TotalDataVagon, Excel

admin.site.register(Locomotiv)
admin.site.register(VagonResistanceConstant)
admin.site.register(Excel)


@admin.register(TotalDataVagon)
class TotalDataVagonAdmin(admin.ModelAdmin):
    pass