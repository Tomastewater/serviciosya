from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'Nombre categoria: {self.nombre}'
    

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nombre servicio: {self.nombre} \nDescripcion: {self.descripcion}"

class ServicioPrestado(models.Model):
    prestador = models.ForeignKey("prestador.Prestador", on_delete=models.CASCADE)
    barrio = models.ForeignKey("ubicacion.Barrio", on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Servicio prestado: {self.servicio.nombre}'

