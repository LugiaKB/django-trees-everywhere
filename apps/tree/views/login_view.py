from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    template_name = "../templates/login.html"
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("home")  # Redirecione para a página após o login
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Please, correct the errors below.")

        return render(request, self.template_name, {"form": form})
