from django.contrib import admin

from station.models import SortingRoadSpecialization, Station, StationRoad, Vagon, NaturalList


@admin.register(SortingRoadSpecialization)
class SortingRoadSpecializationAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(SortingRoadSpecializationAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['single_point'].required = False
        form.base_fields['start_point'].required = False
        form.base_fields['end_point'].required = False
        return form


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(StationRoad)
class StationRoadAdmin(admin.ModelAdmin):
    pass


@admin.register(NaturalList)
class NaturalListAdmin(admin.ModelAdmin):
    pass


@admin.register(Vagon)
class VagonAdmin(admin.ModelAdmin):
    pass
