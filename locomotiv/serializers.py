from rest_framework import serializers
from rest_framework.response import Response


class NumberSerializer(serializers.Serializer):
    number = serializers.CharField()

    def validate(self, attrs):
        number = attrs['number']
        if not len(number) == 8:
            return Response({"error_message": "Iltimos 8 xonali son kiriting!!!"})
        if not number.isnumeric():
            return Response({"error_message": "Iltimos raqam kiriting!!!"})
        sum = 0
        for num in number:
            if int(num) % 2 == 1:
                sum += int(num) * 2
            else:
                sum += int(num) * 1
        check = (int(str(sum)[:1]) + 1) * 10 - sum
        if not check == int(number[-1:]):
            return Response({"error_message": "Vagon raqami noto'g'ri kirtildi, Iltimos tekshirib qaytadan kiriting!!!"})
        return attrs