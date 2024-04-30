from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    
]
