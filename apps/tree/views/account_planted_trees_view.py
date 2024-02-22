from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View


class AccountPlantedTreesView(View):
    template_name = "../templates/planted_trees/planted_trees.html"

    @method_decorator(login_required)
    def get(self, request):
        accounts = request.user.accounts.all()

        planted_trees = set(
            [
                planted_tree
                for account in accounts
                for planted_tree in account.get_planted_trees()
            ]
        )

        context = {"planted_trees": planted_trees, "account_listing": True}

        return render(request, self.template_name, context)
