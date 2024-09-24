from django.db import models
from apps.rol.models import Rol

class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    direccion_real = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"