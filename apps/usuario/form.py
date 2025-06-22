from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Rol
from apps.consumidor.models import Consumidor
from apps.prestador.models import Prestador

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")
    eleccion = forms.ChoiceField(choices=Rol.ROLES, required=True)
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'telefono', 'contraseña']
    
    def clean_email(self):
        """
        Validación para verificar si el correo ya está en uso.
        Si ya está en uso, lanza un error de validación.
        """
        email = self.cleaned_data['email']
        
        # Verificar si el correo ya existe
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado. Prueba con otro")
        
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['contraseña'])  # Cifra la contraseña
        
        # Asigna el email como el valor del campo 'username' si no está vacío
        usuario.username = usuario.email

        if commit:
            usuario.save()
            rol = Rol.objects.create(usuario=usuario, rol=int(self.cleaned_data['eleccion']))

            # Crear un modelo asociado según el rol seleccionado
            if rol.rol == 1:  # Consumidor
                Consumidor.objects.create(rol_usuario=rol)
            elif rol.rol == 2:  # Prestador
                Prestador.objects.create(rol_usuario=rol)
        return usuario