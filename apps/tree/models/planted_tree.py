from django.db import models
from django.utils import timezone


from .tree import Tree
from .user import User
from dateutil.relativedelta import relativedelta


class PlantedTree(models.Model):
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="planted_trees"
    )
    tree = models.ForeignKey(
        Tree, on_delete=models.CASCADE, related_name="planted_trees"
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    @property
    def age(self):
        now = timezone.now()
        difference = relativedelta(now, self.planted_at)

        years = difference.days // 365
        months = (difference.days % 365) // 30
        days = (difference.days % 365) % 30

        age_dict = {
            "years": years,
            "months": months,
            "days": days,
        }

        return age_dict

    @property
    def accounts(self):
        return sorted(self.user.accounts.all(), key=lambda account: account.name)

    def __str__(self):
        return (f"{self.user.__str__()} - {self.tree.name}: {self.planted_at}").strip()

    class Meta:
        app_label = "tree"
