from django import forms

from . import models

class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields = "__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

