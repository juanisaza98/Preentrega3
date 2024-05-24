from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
from . import models, forms

def home(request):
    consulta_pedidos = models.InfoProductoPedido.objects.all()
    context = {"pedidos":consulta_pedidos}
    return render(request, "pedido/index.html", context)

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            # Redirigir a una página específica si el usuario está autenticado pero no es staff
            return redirect('pedido:home')
        else:
            # Dejar el comportamiento por defecto (redirigir a la página de login)
            return super().handle_no_permission()


class PedidoCreate(StaffRequiredMixin, CreateView):
    model = models.InfoProductoPedido
    form_class = forms.InfoProductoPedidoForm
    template_name = 'pedido/pedido_create.html'
    success_url = reverse_lazy('pedido:home')
    


class PedidoDetail(LoginRequiredMixin, DetailView):
    model = models.InfoProductoPedido
    context_object_name = 'pedido'


class PedidoUpdate(StaffRequiredMixin, UpdateView):
    model = models.InfoProductoPedido
    form_class = forms.InfoProductoPedidoForm
    template_name = 'pedido/pedido_update.html'
    success_url = reverse_lazy('pedido:home')


class PedidoDelete(StaffRequiredMixin, DeleteView):
    model = models.InfoProductoPedido
    template_name = 'pedido/pedido_delete.html'
    success_url = reverse_lazy('pedido:home')
    