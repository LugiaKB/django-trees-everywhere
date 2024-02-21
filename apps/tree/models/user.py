from django.contrib.auth.models import User
from django.apps import apps


class User(User):
    def __str__(self):
        return (f"{self.first_name} {self.last_name}").strip() or self.username

    def plant_tree(self, tree, location):
        PlantedTree = apps.get_model("tree", "PlantedTree")

        return PlantedTree.objects.create(
            user=self,
            tree=tree,
            lagitude=location[0],
            longitude=location[1],
        )

    def plant_trees(self, plants):
        PlantedTree = apps.get_model("tree", "PlantedTree")

        planted_trees = [
            PlantedTree(
                user=self,
                tree=tree,
                lagitude=location[0],
                longitude=location[1],
            )
            for tree, location, account in plants
        ]

        PlantedTree.objects.bulk_create(planted_trees)

        return planted_trees

    class Meta:
        app_label = "tree"
        proxy = True
