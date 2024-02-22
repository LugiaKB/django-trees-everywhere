from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    HomeView,
    PlantedTreesView,
    PlantedTreeView,
    AccountPlantedTreesView,
    PlantTreeView,
)

urlpatterns = [
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
    path("plant-tree/", PlantTreeView.as_view(), name="plant-tree"),
]
