from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("categoria/detail/<int:pk>", views.categoria_detail, name="categoria_detail"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("categoria/update/<int:pk>", views.categoria_update, name="categoria_update"),
    path("producto/update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    path("categoria/delete/<int:pk>", views.categoria_delete, name="categoria_delete"),
    path("producto/delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
]
