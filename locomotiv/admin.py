from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from .models import Locomotiv, VagonResistanceConstant, TotalDataVagon, TrainResistanceData, RailwaySwitchMark, \
    RailRoadCharacteristic, WeightModel

admin.site.register(Locomotiv)
admin.site.register(VagonResistanceConstant)
admin.site.register(TrainResistanceData)
admin.site.register(RailwaySwitchMark)
admin.site.register(RailRoadCharacteristic)
admin.site.register(WeightModel)


@admin.register(TotalDataVagon)
class TotalDataVagonAdmin(admin.ModelAdmin):
    pass