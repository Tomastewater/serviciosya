from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'Provincia: {self.nombre}'
    
class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f'Localidad: {self.nombre}'
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'

class Direccion(models.Model):
    calle = models.TextField(max_length=200)
    altura = models.TextField(max_length=200)
    departamento = models.CharField(max_length=100, null=True, default='N/A')
    codigo_postal = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return f"""Calle: {self.calle}
        Altura: {self.altura}
        Departamento: {self.departamento}"""
    
class DireccionConsumidor(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    consumidor = models.ForeignKey("consumidor.Consumidor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.direccion.barrio}, {self.direccion.calle}, {self.direccion.altura}"
