from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import PlantedTree
from ..serializers import PlantedTreeSerializer


class PlantedTreesViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return PlantedTree.objects.filter(user=self.request.user)

    @extend_schema(responses=PlantedTreeSerializer)
    def list(self, request):
        serializer = PlantedTreeSerializer(self.get_queryset(), many=True)
        for plant in serializer.data:
            print(plant["latitude"] + plant["longitude"])
        return Response(serializer.data)
