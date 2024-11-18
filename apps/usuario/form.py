from datetime import datetime
from django import forms
from .models import Usuario, Rol
from apps.consumidor.models import Consumidor
from apps.prestador.models import Prestador
from django.core.exceptions import ValidationError

class usuarioForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True)
    eleccion = forms.ChoiceField(choices=Rol.ROLES, required=True)

    def save(self):
        if Usuario.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")  # Lanza un error si el correo ya existe
        else:

            fecha = datetime.now()
            usuario = Usuario.objects.create(
                nombre = self.cleaned_data['nombre'],
                apellido = self.cleaned_data['apellido'],
                email = self.cleaned_data['email'],
                contraseña = self.cleaned_data['contraseña'],
                fecha_creacion = fecha,
            )
            rol = Rol.objects.create(
                usuario = usuario,
                rol = int(self.cleaned_data['eleccion']),
            )

            if rol.rol == 1:  # Consumidor
                consumidor = Consumidor.objects.create(rol_usuario=rol)
                print(f"Consumidor creado: {consumidor.rol_usuario.usuario.nombre}")
            elif rol.rol == 2:  # Prestador
                prestador = Prestador.objects.create(rol_usuario=rol)
                print(f"Prestador creado: {prestador.rol_usuario.usuario.nombre}")
            else:
                raise ValidationError("Rol no válido.")
            




