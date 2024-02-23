from rest_framework import serializers

from ..models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = PlantedTree
        fields = "__all__"
        read_only_fields = ("user",)

    def get_latitude(self, obj):
        return "{:.6f}".format(obj.latitude)

    def get_longitude(self, obj):
        return "{:.6f}".format(obj.longitude)
