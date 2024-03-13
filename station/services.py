import pyexcel
from django.db.models import Q

from station.models import NaturalList, SortingRoadSpecialization, Vagon


class NaturalListService:
    def __init__(self, natural_list: NaturalList):
        self.natural_list = natural_list

    def import_data(self, file_path):
        data = pyexcel.get_array(file_name=file_path)
        for row in data:
            # first element is sequence of numbers in natural list
            # so we can extract data from it
            # exp: 01 98023450 0201 026 72271  00300 0012 0 6 5 0 02/00 00000 000 OXPAHA
            data = self.extract_data(row[0])
            if data:
                self.create_vagon(data)

    def extract_data(self, string: str):
        """
        :param string: 01 98023450 0201 026 72271  00300 0012 0 6 5 0 02/00 00000 000 OXPAHA
        """
        list_data = string.split()
        if list_data:
            data = {
                "order": int(list_data[0]),
                "number_vagon": list_data[1],
                "load_weight": float(list_data[3]),
                "destination_station": list_data[4],
            }
            road_number = self.get_road_number(data['destination_station'])
            data['road_number'] = road_number
            return data

    def get_road_number(self, destination_station):
        interval = SortingRoadSpecialization.objects.filter(
            Q(single_point=destination_station) |
            Q(
                Q(start_point__lte=destination_station) &
                Q(end_point__gte=destination_station)
            )
        ).first()
        return interval.road.number if interval else None

    def create_vagon(self, data):
        Vagon.objects.create(
            order=data['order'],
            natural_list=self.natural_list,
            number_vagon=data['number_vagon'],
            load_weight=data['load_weight'],
            destination_station=data['destination_station'],
            road_number_id=data['road_number'],
        )  # TODO: Get other data and save it to the model

