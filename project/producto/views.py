from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def home(request):
    consulta_categorias = models.ProductoCategoria.objects.all()
    consulta_productos = models.Producto.objects.all()
    context = {"categorias":consulta_categorias, "productos":consulta_productos}
    return render(request, "producto/index.html", context)

def categoria_create(request):
    if request.method == "POST":
        form_categoria_create = forms.ProductoCategoriaForm(request.POST)
        if form_categoria_create.is_valid():
            form_categoria_create.save()
            return redirect("producto:home")
    else:
        form_categoria_create = forms.ProductoCategoriaForm()
    return render(request, "producto/categoria_create.html", context={"form_categoria_create": form_categoria_create})

def producto_create(request):
    if request.method == "POST":
        form_producto_create = forms.ProductoForm(request.POST)
        if form_producto_create.is_valid():
            form_producto_create.save()
            return redirect("producto:home")
    else:
        form_producto_create = forms.ProductoForm()
    return render(request, "producto/producto_create.html", context={"form_producto_create": form_producto_create})
