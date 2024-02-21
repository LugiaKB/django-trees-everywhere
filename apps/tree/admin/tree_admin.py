from django.contrib import admin
from ..models import Tree, PlantedTree


class PlantedTreeInline(admin.TabularInline):
    model = PlantedTree
    extra = 1


class TreeAdmin(admin.ModelAdmin):
    inlines = [PlantedTreeInline]


admin.site.register(Tree, TreeAdmin)
