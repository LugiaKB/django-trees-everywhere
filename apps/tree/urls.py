from django.urls import path
from .views.auth.login_view import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
