from django import forms

from . import models

class InfoProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = models.InfoProductoPedido
        fields = "__all__"
