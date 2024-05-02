from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    path("producto/create/", views.producto_create, name="producto_create"),
]
