from django.urls import path

app_name = "pedido"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("pedido/create/", views.PedidoCreate.as_view(), name="pedido_create"),
    path("pedido/detail/", views.PedidoDetail.as_view(), name="pedido_detail"),
    path("pedido/update/", views.PedidoUpdate.as_view(), name="pedido_update"),
    path("pedido/delete/", views.PedidoDelete.as_view(), name="pedido_delete"),
    
]
