from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View


class PlantedTreesView(View):
    template_name = "../templates/planted_trees.html"

    @method_decorator(login_required)
    def get(self, request):
        user = request.user

        planted_trees = user.planted_trees.all()

        context = {"planted_trees": planted_trees}

        return render(request, self.template_name, context)
