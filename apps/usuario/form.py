from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario, Rol
from apps.consumidor.models import Consumidor
from apps.prestador.models import Prestador

class UsuarioForm(forms.ModelForm):
    """
    Formulario para registrar un nuevo usuario.

    Permite ingresar nombre, apellido, email, contraseña y seleccionar el rol (Consumidor o Prestador).
    Valida que el email no esté registrado y crea el modelo asociado según el rol.
    """
    contraseña = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")
    eleccion = forms.ChoiceField(choices=Rol.ROLES, required=True)
    
    class Meta:
        """
        Configuración del formulario asociada al modelo Usuario.
        """
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'contraseña']
    
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
        """
        Guarda el usuario, cifra la contraseña y crea el modelo asociado según el rol seleccionado.

        Args:
            commit (bool): Si True, guarda el usuario en la base de datos.

        Returns:
            Usuario: La instancia de usuario creada.
        """
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