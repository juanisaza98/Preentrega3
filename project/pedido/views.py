from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def home(request):
    consulta_pedidos = models.InfoProductoPedido.objects.all()
    context = {"pedidos":consulta_pedidos}
    return render(request, "pedido/index.html", context)

def pedido_create(request):
    if request.method == "POST":
        form_pedido_create = forms.InfoProductoPedidoForm(request.POST)
        if form_pedido_create.is_valid():
            form_pedido_create.save()
            return redirect("pedido:home")
    else:
        form_pedido_create = forms.InfoProductoPedidoForm()
    return render(request, "pedido/pedido_create.html", context={"form_pedido_create": form_pedido_create})