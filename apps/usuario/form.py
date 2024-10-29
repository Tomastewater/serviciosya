from django import forms
from .models import Usuario

class usuarioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    email = forms.EmailField(unique=True)
    contraseña = forms.CharField(max_length=128)
    fecha_creacion = forms.DateTimeField(auto_now_add=True)

    def save(self):
        Usuario.objects.create(
            nombre = self.cleaned_data['nombre'],
            apellido = self.cleaned_data['apellido'],
            email = self.cleaned_data['email'],
            contraseña = self.cleaned_data['contraseña'],
            fecha_creacion = self.cleaned_data['fecha_creacion'],
        )