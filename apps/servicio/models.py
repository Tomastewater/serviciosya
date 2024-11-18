from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'
    

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.categoria}"

class ServicioPrestado(models.Model):
    prestador = models.ForeignKey("prestador.Prestador", on_delete=models.CASCADE)
    localidad = models.ForeignKey("ubicacion.Localidad", on_delete=models.CASCADE, default=None)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.servicio.nombre} - Prestado por: {self.prestador.rol_usuario.usuario.nombre} {self.prestador.rol_usuario.usuario.apellido} en {self.localidad}'

