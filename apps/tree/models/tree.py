from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    image_source = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.scientific_name})"

    class Meta:
        app_label = "tree"
