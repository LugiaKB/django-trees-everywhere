from django.db import models

from .user import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name="accounts", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "tree"
