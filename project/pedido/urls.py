from django.urls import path

app_name ="pedido"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    
]
