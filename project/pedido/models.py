from django.db import models
from cliente.models import Cliente
from producto.models import Producto
# Create your models here.
class InfoProductoPedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False, verbose_name="cliente")
    producto_pedido = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=False, null=False, verbose_name="producto")

    def precio(self):
        return self.producto_pedido.precio

    def __str__(self):
        return f"Cliente:{self.cliente} | Producto pedido:{self.producto_pedido} | Valor a pagar: {self.producto_pedido.precio}"