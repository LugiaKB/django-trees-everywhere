from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = "../templates/home.html"

    @method_decorator(login_required)
    def get(self, request):
        context = {
            "username": request.user.username,
            "about": request.user.profile.about,
        }

        return render(request, self.template_name, context)
