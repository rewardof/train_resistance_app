from rest_framework import serializers


class ProcessNaturalListSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    name = serializers.CharField(
        required=True,
        help_text="Name of Natural List"
    )
    code = serializers.CharField(
        required=True,
        help_text="Code of Natural List"
    )
