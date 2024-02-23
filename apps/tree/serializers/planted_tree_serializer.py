from rest_framework import serializers

from ..models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantedTree
        fields = "__all__"
        read_only_fields = ("user",)
