from django.db import models
from django.contrib.auth.hashers import make_password

class Rol(models.Model):
    ROLES = [
        (1,'Quiero contratar un servicio'),
        (2,'Quiero prestar servicio')
    ]

    rol = models.IntegerField(choices=ROLES)
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, related_name="rols") 
    
    def __str__(self):
        return f'Nombre: {self.usuario.nombre} | Rol: {'Consumidor' if self.rol == 1 else 'Prestador de servicio'}'
    


class Usuario(models.Model):
    
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Correo: {self.email}"
    

"ATOMICS TRANSACTIONS"