from rest_framework import serializers
from rest_framework.response import Response

from locomotiv.models import Locomotiv, TotalDataVagon, Excel


class NumberSerializer(serializers.Serializer):
    number = serializers.CharField()
    load_weight = serializers.FloatField()

    def validate(self, attrs):
        number = attrs['number']
        if not len(number) == 8:
            raise serializers.ValidationError({"error_message": "Iltimos 8 xonali son kiriting!!!"})
        if not number.isnumeric():
            raise serializers.ValidationError({"error_message": "Iltimos raqam kiriting!!!"})
        sum = 0
        for num in number:
            if int(num) % 2 == 1:
                sum += int(num) * 2
            else:
                sum += int(num) * 1
        check = (int(str(sum)[:1]) + 1) * 10 - sum
        print(sum)
        # if not check == int(number[-1:]):
        #     raise serializers.ValidationError({"error_message": "Vagon raqami noto'g'ri kirtildi, Iltimos tekshirib qaytadan kiriting!!!"})
        return attrs


class TotalDataSerializer(serializers.Serializer):
    number_vagon = serializers.IntegerField()
    number_of_arrow = serializers.IntegerField()
    netto_vagon = serializers.FloatField()
    length_vagon = serializers.FloatField()
    total_weight = serializers.FloatField()
    bullet_weight = serializers.FloatField()

    class Meta:
        model = TotalDataVagon
        fields = ['id', 'number_vagon', 'number_of_arrow', 'netto_vagon', 'length_vagon', 'total_weight', 'bullet_weight']
    
    def create(self, validated_data):
        return TotalDataVagon.objects.create(**validated_data)


class InputDataSerializer(serializers.Serializer):
    number_of_arrow = serializers.IntegerField()
    netto_vagon = serializers.FloatField()
    length_vagon = serializers.FloatField()


class LocomotivSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locomotiv
        fields = ['id', 'locomotiv_name', 'locomotiv_seria', 'locomotiv_number', 'type_locomotiv']


class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excel
        fields = ['file',]
