from django import forms
from .models import ServicioPrestado

class ServicioPrestadoForm(forms.ModelForm):
    """
    Formulario para crear o editar un ServicioPrestado.

    Permite ingresar la categoría, localidad, precio, imagen y descripción del servicio.
    """
    class Meta:
        """
        Configuración del formulario asociada al modelo ServicioPrestado.
        """
        model = ServicioPrestado
        fields = ['categoria', 'localidad', 'precio', 'imagen', 'descripcion']