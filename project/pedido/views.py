from django.shortcuts import render

# Create your views here.
from . import models

def home(request):
    consulta_pedidos = models.InfoProductoPedido.objects.all()
    context = {"pedidos":consulta_pedidos}
    return render(request, "pedido/index.html", context)