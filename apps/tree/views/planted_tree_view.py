from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View

from ..models import PlantedTree


class PlantedTreeView(View):
    template_name = "../templates/planted_tree/planted_tree.html"

    @method_decorator(login_required)
    def get(self, request, pk=None):

        planted_tree = PlantedTree.objects.get(pk=pk)

        context = {"planted_tree": planted_tree}

        return render(request, self.template_name, context)
