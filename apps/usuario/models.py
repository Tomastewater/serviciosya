from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    """
    Modelo personalizado de usuario que extiende AbstractUser.

    Atributos:
        nombre (CharField): Nombre del usuario.
        apellido (CharField): Apellido del usuario.
        email (EmailField): Correo electrónico único del usuario.
        fecha_creacion (DateTimeField): Fecha y hora de creación del usuario.
    """
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    apellido = models.CharField(max_length=150, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']
    
    def __str__(self):
        """
        Retorna una representación legible del usuario.
        """
        return f"{self.nombre} {self.apellido} ({self.email})"
    
    
class Rol(models.Model):
    """
    Modelo que representa el rol de un usuario en la plataforma.

    Atributos:
        ROLES (list): Opciones de roles disponibles (Consumidor o Prestador).
        rol (IntegerField): Rol asignado al usuario.
        usuario (ForeignKey): Referencia al usuario asociado.
    """
    ROLES = [
        (1, 'Quiero contratar un servicio'),
        (2, 'Quiero prestar servicio')
    ]

    rol = models.IntegerField(choices=ROLES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        """
        Retorna una representación legible del rol.
        """
        return f"Rol: {'Consumidor' if self.rol == 1 else 'Prestador de servicio'}"