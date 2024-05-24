from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from .forms import CustomAuthenticationForm, CustomUserCreationForm

# Create your views here.
from . import models


def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form":form})