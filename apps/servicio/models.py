from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Categoria(models.Model):
    """
    Modelo que representa una categoría de servicios.
    
    Atributos:
        nombre (CharField): Nombre de la categoría.
    """
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'
    

class Servicio(models.Model):
    """
    Modelo que representa un servicio general.

    Atributos:
        nombre (CharField): Nombre del servicio.
        descripcion (TextField): Descripción del servicio (opcional).
        categoria (ForeignKey): Categoría a la que pertenece el servicio.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.categoria}"

class ServicioPrestado(models.Model):
    """
    Modelo que representa un servicio ofrecido por un prestador en una localidad específica.

    Atributos:
        prestador (ForeignKey): Prestador que ofrece el servicio.
        localidad (ForeignKey): Localidad donde se ofrece el servicio.
        categoria (ForeignKey): Categoría del servicio ofrecido.
        precio (DecimalField): Precio del servicio (opcional).
        imagen (ImageField): Imagen ilustrativa del servicio (opcional).
        descripcion (TextField): Descripción adicional del servicio (opcional).
    """
    prestador = models.ForeignKey("prestador.Prestador", on_delete=models.CASCADE)
    localidad = models.ForeignKey("ubicacion.Localidad", on_delete=models.CASCADE, default=None)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='servicios_prestados/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.categoria.nombre} - Prestado por: {self.prestador.rol_usuario.usuario.nombre} {self.prestador.rol_usuario.usuario.apellido} en {self.localidad}'

@receiver(post_delete, sender=ServicioPrestado)
def eliminar_imagen_servicio(sender, instance, **kwargs):
    """
    Elimina la imagen asociada a un ServicioPrestado del sistema de archivos cuando se elimina la instancia.

    Parámetros:
        sender: El modelo que envía la señal.
        instance: La instancia de ServicioPrestado que fue eliminada.
        **kwargs: Argumentos adicionales.
    """
    if instance.imagen and instance.imagen.path:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)
