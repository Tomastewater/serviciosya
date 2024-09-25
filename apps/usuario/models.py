from django.db import models
from django.contrib.auth.hashers import make_password
from rol.models import Rol

class Usuario(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING, null=False)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
    
    def set_password(self, password):
        """
        Cifra la contraseña y la guarda en el campo `contraseña`.
        """
        self.contraseña = make_password(password)
        self.save()