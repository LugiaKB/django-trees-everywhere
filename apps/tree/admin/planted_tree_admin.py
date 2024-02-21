from django.contrib import admin
from ..models import PlantedTree


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ("tree", "user", "accounts", "planted_at")


admin.site.register(PlantedTree, PlantedTreeAdmin)
