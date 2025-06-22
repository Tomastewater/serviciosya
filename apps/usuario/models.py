from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    apellido = models.CharField(max_length=150, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
    
    
class Rol(models.Model):
    ROLES = [
        (1, 'Quiero contratar un servicio'),
        (2, 'Quiero prestar servicio')
    ]

    rol = models.IntegerField(choices=ROLES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        return f"Rol: {'Consumidor' if self.rol == 1 else 'Prestador de servicio'}"