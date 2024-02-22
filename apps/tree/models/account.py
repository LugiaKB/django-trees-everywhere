from django.db import models

from .user import User


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name="accounts", blank=True)

    def __str__(self):
        return self.name

    def get_planted_trees(self):
        planted_trees = [
            planted_tree
            for user in self.users.all()
            for planted_tree in user.planted_trees.all()
        ]

        return set(planted_trees)

    class Meta:
        app_label = "tree"
