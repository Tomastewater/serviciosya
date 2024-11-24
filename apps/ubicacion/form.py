from django import forms
from apps.ubicacion.models import Localidad, Provincia, Direccion
from django.core.exceptions import ValidationError
class DireccionForm(forms.Form):
    calle = forms.CharField(max_length=150, required=True)
    altura = forms.IntegerField()
    departamento = forms.CharField(max_length=150, required=True)
    codigo_postal = forms.CharField(max_length=150)
    provincia = forms.ChoiceField(choices=Provincia.PROVINCIAS, required=True)
    barrio = forms.CharField(max_length=150)
    localidad = forms.CharField(max_length=150, required=True)

    def save(self, commit=True):
        # Verifica si la dirección ya existe
        if Direccion.objects.filter(calle=self.cleaned_data['calle'], altura=self.cleaned_data['altura']).exists():
            raise ValidationError("Esta direccion ya esta registrada")  # Lanza un error si la calle y la altura ya existen
        
        # Crea la provincia
        provincia = Provincia.objects.create(
            nombre=self.cleaned_data['provincia'],
        )
        
        # Crea la localidad
        localidad = Localidad.objects.create(
            nombre=self.cleaned_data['localidad'],
            provincia=provincia,
        )
        
        # Crea la dirección y, si commit=True, guarda en la base de datos
        direccion = Direccion(
            calle=self.cleaned_data['calle'],
            altura=self.cleaned_data['altura'],
            departamento=self.cleaned_data['departamento'],
            codigo_postal=self.cleaned_data['codigo_postal'],
            barrio=self.cleaned_data['barrio'],
            localidad=localidad,
        )

        if commit:
            direccion.save()  # Guarda la dirección en la base de datos si commit es True

        return direccion

"""

class DireccionForm(forms.Form):
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
            Direccion = Direccion.objects.create(
            calle = self.cleaned_data['calle'],
            altura = self.cleaned_data['altura'],
            departamento = self.cleaned_data['departamento'],
            codigo_postal = self.cleaned_data['codigo_postal'],
            barrio = self.cleaned_data['barrio'],
            localidad = localidad,
            )
"""            
