from django.urls import path, include

from .views import (
    LoginView,
    LogoutView,
    HomeView,
    PlantedTreesView,
    PlantedTreeView,
    AccountPlantedTreesView,
    PlantTreeView,
)
from .api_urls import api_urls

urlpatterns = [
    path("api/", include(api_urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", HomeView.as_view(), name="home"),
    path("planted-trees/", PlantedTreesView.as_view(), name="planted-trees"),
    path("planted-trees/<int:pk>/", PlantedTreeView.as_view(), name="planted-tree"),
    path(
        "planted-trees/account/",
        AccountPlantedTreesView.as_view(),
        name="account-planted-trees",
    ),
    path("planted-trees/add", PlantTreeView.as_view(), name="plant-tree"),
]
