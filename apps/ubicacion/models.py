from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'Provincia: {self.nombre}'
    
class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey("ubicacion.Provincia", on_delete=models.CASCADE)

    def __str__(self):
        return f'Localidad: {self.nombre}'
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey("ubicacion.Localidad", on_delete=models.CASCADE)

    def __str__(self):
        return f'Barrio: {self.nombre}'

class Direccion(models.Model):
    calle = models.TextField(max_length=50)
    altura = models.TextField(max_length=6)
    departamento = models.CharField(max_length=5, null=True, default='N/A')
    codigo_postal = models.CharField(max_length=10)
    barrio = models.ForeignKey("ubicacion.Barrio", on_delete=models.CASCADE)

    def __str__(self):
        return f"""Calle: {self.calle}
        Altura: {self.altura}
        Departamento: {self.departamento}
        Barrio: {self.barrio}"""
    
class DireccionConsumidor(models.Model):
    direccion = models.ForeignKey("ubicacion.Direccion", on_delete=models.CASCADE)
    consumidor = models.ForeignKey("consumidor.Consumidor", on_delete=models.CASCADE)
