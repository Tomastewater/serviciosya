from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    ROLES = [
        (1,'Quiero contratar un servicio'),
        (2,'Quiero prestar servicio')
    ]

    rol = models.IntegerField(choices=ROLES)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=10, default="0000000000")
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni}"
    
    def set_password(self, password):
        """
        Cifra la contraseña y la guarda en el campo `contraseña`.
        """
        self.contraseña = make_password(password)
        self.save()

