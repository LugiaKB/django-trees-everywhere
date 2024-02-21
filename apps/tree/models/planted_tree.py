from django.db import models
from django.utils import timezone

from .tree import Tree
from .user import User


class PlantedTree(models.Model):
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="planted_trees"
    )
    tree = models.OneToOneField(
        Tree, on_delete=models.CASCADE, related_name="planted_trees"
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    @property
    def age(self):
        now = timezone.now()
        return (now - self.planted_at).years

    @property
    def accounts(self):
        return sorted(list(self.user.accounts.values_list("name", flat=True)))

    @property
    def location(self):
        return (self.latitude, self.longitude)

    def __str__(self):
        return (f"{self.user.__str__()} - {self.tree.name}: {self.planted_at}").strip()

    class Meta:
        app_label = "tree"
