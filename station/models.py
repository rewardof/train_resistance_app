from django.db import models

from utils.constants import CONSTANTS


class SortingRoadSpecialization(models.Model):
    # either single_point or start_point and end_point should be filled
    single_point = models.IntegerField(null=True)
    start_point = models.IntegerField(null=True)
    end_point = models.IntegerField(null=True)
    road = models.ForeignKey('StationRoad', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.single_point:
            return f"{self.single_point} -->> {self.road.number}-yo'l"
        else:
            return f"{self.start_point} - {self.end_point} -->> {self.road.number}-yo'l"


class Station(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class StationRoad(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    number = models.IntegerField()
    type = models.CharField(choices=CONSTANTS.ROAD_TYPE.CHOICES, max_length=16)

    def __str__(self):
        return f"{self.station} - {self.number} - {self.type}"


class NaturalList(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Vagon(models.Model):
    natural_list = models.ForeignKey(NaturalList, on_delete=models.CASCADE)
    number_vagon = models.IntegerField("Vagon raqami")
    vagon_type = models.CharField(choices=CONSTANTS.VAGON_TYPE.CHOICES, max_length=8, null=True)
    load_weight = models.FloatField("Yuk og'irligi", null=True)
    number_of_arrow = models.SmallIntegerField("O'qlar soni", null=True)
    netto_vagon = models.FloatField("Vagon og'irligi", null=True)
    length_vagon = models.FloatField("Vagon uzunligi", null=True)
    total_weight = models.FloatField("Umumiy og'irlik", null=True)
    bullet_weight = models.FloatField("O'qqa tushadigan og'irlik", null=True)
    destination_station = models.CharField(max_length=5, null=True)
    road_number = models.ForeignKey(
        StationRoad, null=True,
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.number_vagon}-{self.natural_list.name}"