from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View


from ..models import Tree


class PlantTreeView(View):
    template_name = "../templates/plant_tree.html"

    @method_decorator(login_required)
    def get(self, request):

        available_trees = Tree.objects.all()

        context = {"available_trees": available_trees}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):

        tree_id = request.POST.get("tree_id")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        user = request.user

        planted_tree = user.plant_tree(tree_id, (latitude, longitude))

        return redirect("planted-tree", pk=planted_tree.pk)
