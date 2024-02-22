from django.apps import apps
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="tree_user_groups",  # Adicione esta linha
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="tree_user_permissions",  # Adicione esta linha
    )

    def __str__(self):
        return (f"{self.first_name} {self.last_name}").strip() or self.username

    def plant_tree(self, tree_id, location):
        PlantedTree = apps.get_model("tree", "PlantedTree")

        return PlantedTree.objects.create(
            user=self,
            tree_id=tree_id,
            latitude=location[0],
            longitude=location[1],
        )

    def plant_trees(self, plants):
        PlantedTree = apps.get_model("tree", "PlantedTree")

        planted_trees = [
            PlantedTree(
                user=self,
                tree_id=tree_id,
                latitude=location[0],
                longitude=location[1],
            )
            for tree_id, location, account in plants
        ]

        PlantedTree.objects.bulk_create(planted_trees)

        return planted_trees

    class Meta:
        app_label = "tree"
