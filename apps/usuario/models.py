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
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Correo: {self.email}"
    
    def set_password(self, password):
        """
        Cifra la contraseña y la guarda en el campo `contraseña`.
        """
        self.contraseña = make_password(password)
        self.save()

