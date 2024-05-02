from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def home(request):
    consulta_clientes = models.Cliente.objects.all()
    consulta_paises = models.Pais.objects.all()
    context = {"clientes":consulta_clientes, "paises":consulta_paises}
    return render(request, "cliente/index.html", context)

def pais_create(request):
    if request.method == "POST":
        form_pais_create = forms.PaisForm(request.POST)
        if form_pais_create.is_valid():
            form_pais_create.save()
            return redirect("cliente:home")
    else:
        form_pais_create = forms.PaisForm()
    return render(request, "cliente/pais_create.html", context={"form_pais_create": form_pais_create})

def cliente_create(request):
    if request.method == "POST":
        form_cliente_create = forms.ClienteForm(request.POST)
        if form_cliente_create.is_valid():
            form_cliente_create.save()
            return redirect("cliente:home")
    else:
        form_cliente_create = forms.ClienteForm()
    return render(request, "cliente/cliente_create.html", context={"form_cliente_create": form_cliente_create})
