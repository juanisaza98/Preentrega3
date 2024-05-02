from django.urls import path

app_name ="pedido"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("pedido/create/", views.pedido_create, name="pedido_create"),
    
]
