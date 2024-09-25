from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=100)       #CharField es mas eficiente porque esta optimizado para textos cortos
    descripcion = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} \nDescripcion: {self.descripcion}'