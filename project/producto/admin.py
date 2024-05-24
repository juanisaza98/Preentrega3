from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Productos y categorias"


admin.site.register(models.ProductoCategoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria_producto", "nombre", "descripcion", "precio", "stock_disponible", "fecha_actualizacion" )
    list_display_links = ("nombre",)

admin.site.register(models.Producto, ProductoAdmin)


