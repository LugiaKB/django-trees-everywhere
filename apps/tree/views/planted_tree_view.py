from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.views import View

from ..models import PlantedTree


class PlantedTreeView(View):
    template_name = "../templates/planted_tree/planted_tree.html"

    @method_decorator(login_required)
    def get(self, request, pk=None):
        planted_tree = get_object_or_404(PlantedTree, pk=pk)

        if planted_tree.user != request.user:
            return HttpResponseForbidden(
                "You do not have permission to view this tree."
            )

        context = {"planted_tree": planted_tree}
        return render(request, self.template_name, context)
