from django.db import models

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