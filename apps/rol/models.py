from django.db import models

class Rol(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} \nDescripcion: {self.descripcion}'