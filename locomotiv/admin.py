from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from .models import Locomotiv, VagonResistanceConstant, TotalDataVagon, TrainResistanceData

admin.site.register(Locomotiv)
admin.site.register(VagonResistanceConstant)
admin.site.register(TrainResistanceData)


@admin.register(TotalDataVagon)
class TotalDataVagonAdmin(admin.ModelAdmin):
    pass