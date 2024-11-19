from django import forms
from .models import Direccion, Localidad, Provincia
from apps.ubicacion.models import Direccion
from apps.prestador.models import Prestador
from django.core.exceptions import ValidationError

class direccionForm(forms.Form):
    calle = forms.CharField(max_length=150, required=True)
    altura = forms.IntegerField()
    departamento = forms.CharField(max_length=150, required=True)
    codigo_postal = forms.CharField(max_length=150)
    provincia = forms.ChoiceField(choices=Provincia.PROVINCIAS, required=True)
    barrio = forms.CharField(max_length=150)
    localidad = forms.CharField(max_length=150, required=True)

    def save(self):
        if Direccion.objects.filter(calle=self.cleaned_data['calle'], altura=self.cleaned_data['altura']).exists():
            raise ValidationError("Esta direccion ya esta registrada")  # Lanza un error si la calle y ya altura ya existen
        else:

            provincia = Provincia.objects.create(
                nombre = int(self.cleaned_data['provincia']),
            )
            localidad = Localidad.objects.create(
                nombre = self.cleaned_data['localidad'],
                provincia = provincia
            )

            direccion = Direccion.objects.create(
                calle = self.cleaned_data['calle'],
                altura = self.cleaned_data['altura'],
                departamento = self.cleaned_data['departamento'],
                codigo_postal = self.cleaned_data['codigo_postal'],
                barrio = self.cleaned_data['barrio'],
                localidad = localidad,
            )
