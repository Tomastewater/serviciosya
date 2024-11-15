
from django import forms
from .models import Consumidor

class consumidorForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    CUIL = forms.CharField(max_length=100)
    numero_telefono = forms.CharField(max_length=100)
