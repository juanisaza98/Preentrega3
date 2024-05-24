from django.db import models
from django.utils import timezone

# Create your models here.
class ProductoCategoria(models.Model):
    """Categorias de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank = True, verbose_name="descripcion")

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre
    
    class Meta:
        verbose_name="categoria de productos"
        verbose_name_plural="categorias de productos"

class Producto(models.Model):
    categoria_producto = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoria de producto")
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank = True, verbose_name="descripcion")
    precio = models.PositiveIntegerField()
    stock_disponible=models.FloatField(default=0)
    imagen = models.ImageField(upload_to="imagenes/", null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de actualizacion")
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
    