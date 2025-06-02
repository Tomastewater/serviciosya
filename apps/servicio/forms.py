from django import forms
from .models import ServicioPrestado

class ServicioPrestadoForm(forms.ModelForm):
    class Meta:
        model = ServicioPrestado
        fields = ['servicio', 'localidad', 'precio', 'imagen', 'descripcion']