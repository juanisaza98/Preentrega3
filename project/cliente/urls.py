from django.urls import path

app_name ="cliente"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("pais/create/", views.pais_create, name="pais_create"),
    path("cliente/create/", views.cliente_create, name="cliente_create"),
    
]
