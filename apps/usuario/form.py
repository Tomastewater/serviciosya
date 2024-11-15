from datetime import datetime
from django import forms
from .models import Usuario, Rol
from django.core.exceptions import ValidationError

class usuarioForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)
    eleccion = forms.ChoiceField(choices=Rol.ROLES, required=True)

    def save(self):
        if Usuario.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        
        fecha = datetime.now()
        usuario_form = Usuario.objects.create(
            nombre = self.cleaned_data['nombre'],
            apellido = self.cleaned_data['apellido'],
            email = self.cleaned_data['email'],
            contraseña = self.cleaned_data['contraseña'],
            fecha_creacion = fecha,
        )
        Rol.objects.create(
            usuario = usuario_form,
            rol = self.cleaned_data['eleccion']
        )
