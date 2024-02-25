from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include

from .api import PlantedTreesViewSet

router = DefaultRouter()

router.register("planted-trees", PlantedTreesViewSet, basename="api-planted-trees")

api_urls = [
    path("", include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
