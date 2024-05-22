from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
from . import models, forms

def home(request):
    consulta_productos = request.GET.get("consulta_productos", None)
    
    if consulta_productos:
        print(consulta_productos)
        query = models.Producto.objects.filter(nombre__icontains=consulta_productos)
    else:
        query = models.Producto.objects.all()
        
    consulta_categorias = models.ProductoCategoria.objects.all()
    context = {"categorias":consulta_categorias, "productos":query}
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

#Producto create en funcion
# def producto_create(request):
#     if request.method == "POST":
#         form_producto_create = forms.ProductoForm(request.POST)
#         if form_producto_create.is_valid():
#             form_producto_create.save()
#             return redirect("producto:home")
#     else:
#         form_producto_create = forms.ProductoForm()
#     return render(request, "producto/producto_create.html", context={"form_producto_create": form_producto_create})

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name = 'producto/producto_create.html'
    success_url = reverse_lazy('producto:home')
    

#Funcion producto detail
# def producto_detail(request, pk: int):
#     query = models.Producto.objects.get(id=pk)
#     return render(request, "producto/producto_detail.html", {"producto": query})

class ProductoDetail(DetailView):
    model = models.Producto
    context_object_name = 'producto'

#Funcion para Update
# def producto_update(request, pk: int):
#     query = models.Producto.objects.get(id=pk)
#     if request.method == "POST":
#         form_producto_update = forms.ProductoForm(request.POST, instance=query)
#         if form_producto_update.is_valid():
#             form_producto_update.save()
#             return redirect("producto:home")
#     else:
#         form_producto_update = forms.ProductoForm(instance=query)
#     return render(request, "producto/producto_update.html", context={"form_producto_update": form_producto_update})

class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name = 'producto/producto_update.html'
    success_url = reverse_lazy('producto:home')

# Funcion producto Delete
# def producto_delete(request, pk: int):
#     query = models.Producto.objects.get(id=pk)
#     if request.method == "POST":
#        query.delete()
#        return redirect("producto:home")
#     return render(request, "producto/producto_delete.html", context={"producto": query})

class ProductoDelete(DeleteView):
    model = models.Producto
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('producto:home')
    