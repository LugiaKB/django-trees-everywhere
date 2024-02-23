from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .api import PlantedTreesViewSet

router = DefaultRouter()

router.register("planted-trees", PlantedTreesViewSet, basename="api-planted-trees")

api_urls = [
    path("", include(router.urls)),
]
