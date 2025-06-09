from django import forms
from apps.ubicacion.models import Localidad, Provincia, Direccion
from django.core.exceptions import ValidationError


class DireccionForm(forms.Form):
    """
    Formulario personalizado para crear una nueva dirección.

    Permite ingresar los datos de la dirección, validando que no exista una igual.
    Si la dirección es nueva, crea la provincia, localidad y la dirección asociada.
    """
    calle = forms.CharField(max_length=150, required=True)
    altura = forms.IntegerField()
    departamento = forms.CharField(max_length=150, required=True)
    codigo_postal = forms.CharField(max_length=150)
    provincia = forms.ChoiceField(choices=Provincia.PROVINCIAS, required=True)
    barrio = forms.CharField(max_length=150)
    localidad = forms.CharField(max_length=150, required=True)

    def save(self, commit=True):
        """
        Guarda la dirección en la base de datos si no existe una igual.

        Lanza ValidationError si ya existe una dirección con la misma calle y altura.
        Crea la provincia y localidad si es necesario.

        Args:
            commit (bool): Si True, guarda la dirección en la base de datos.

        Returns:
            Direccion: La instancia de dirección creada.
        """
        if Direccion.objects.filter(calle=self.cleaned_data['calle'], altura=self.cleaned_data['altura']).exists():
            raise ValidationError("Esta direccion ya esta registrada")  # Lanza un error si la calle y la altura ya existen
        
        provincia = Provincia.objects.create(
            nombre=self.cleaned_data['provincia'],
        )
        
        localidad = Localidad.objects.create(
            nombre=self.cleaned_data['localidad'],
            provincia=provincia,
        )
        
        direccion = Direccion(
            calle=self.cleaned_data['calle'],
            altura=self.cleaned_data['altura'],
            departamento=self.cleaned_data['departamento'],
            codigo_postal=self.cleaned_data['codigo_postal'],
            barrio=self.cleaned_data['barrio'],
            localidad=localidad,
        )

        if commit:
            direccion.save()

        return direccion

class ModificarDireccionForm(forms.ModelForm):
    """
    Formulario para modificar una dirección existente.

    Utiliza el modelo Direccion y permite editar los campos principales.
    """
    class Meta:
        model = Direccion
        fields = ['calle', 'altura', 'departamento', 'codigo_postal', 'barrio', 'localidad']