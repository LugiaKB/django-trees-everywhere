from django.db import models

from .user import User


class Profile(models.Model):
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username} - {self.joined}"

    class Meta:
        app_label = "tree"
