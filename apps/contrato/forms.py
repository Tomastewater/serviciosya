from django import forms
from .models import SolicitudServicio
from apps.ubicacion.models import Direccion

class SolicitudServicioForm(forms.ModelForm):
    fecha_solicitada = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    direccion = forms.ModelChoiceField(queryset=Direccion.objects.none())

    class Meta:
        model = SolicitudServicio
        fields = ['fecha_solicitada', 'direccion']

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['direccion'].queryset = Direccion.objects.filter(usuario=usuario)