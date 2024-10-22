from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'
    
class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}, {self.provincia}'
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} ({self.localidad})'

class Direccion(models.Model):
    calle = models.TextField(max_length=200)
    altura = models.TextField(max_length=200)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        departamento_str = f', Departamento: {self.departamento}' if self.departamento else ''
        return f"""{self.calle} {self.altura}{departamento_str},
        Barrio: {self.barrio}, CP: {self.codigo_postal}"""
    
class DireccionConsumidor(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    consumidor = models.ForeignKey("consumidor.Consumidor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consumidor}, {self.direccion}"
