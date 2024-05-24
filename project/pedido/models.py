from django.db import models
from cliente.models import Cliente
from producto.models import Producto
from django.forms import ValidationError
from django.utils import timezone
# Create your models here.
class InfoProductoPedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False, verbose_name="cliente")
    producto_pedido = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=False, null=False, verbose_name="producto")
    cantidad = models.PositiveIntegerField(default=0)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("fecha_venta",)

    def clean(self) -> None:
        if self.cantidad > self.producto_pedido.stock_disponible:
            raise ValidationError("La cantidad vendida no puede ser mayor a la disponible")
        return super().clean()
    
    def save(self, *args, **kwargs):
        self.precio_total = self.producto_pedido.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cliente:{self.cliente} | Producto pedido:{self.producto_pedido} | | Cantidad: {self.cantidad} unidades | Valor a pagar: {self.precio_total}"