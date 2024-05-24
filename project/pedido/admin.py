from django.contrib import admin

# Register your models here.
from . import models

class InfoProductoAdmin(admin.ModelAdmin):
    list_display = ("cliente",
                    "producto_pedido",
                    "cantidad",
                    "precio_total",
                    "fecha_venta")
    list_display_links = ("producto")
    date_hierarchy = ("fecha_venta")

admin.site.register(models.InfoProductoPedido)
