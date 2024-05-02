from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="pais", unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "paises"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="pais de origen")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

