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
    

class Direccion(models.Model):
    calle = models.TextField(max_length=200)
    altura = models.TextField(max_length=200)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=100)
    barrio = models.CharField(max_length=200, blank=True, null=True, default=None)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, default=None)
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, default=None)

    def __str__(self):
        departamento_str = f', Departamento: {self.departamento}' if self.departamento else ''
        barrio_str = f', Barrio: {self.barrio}' if self.barrio else ''
        return f"""{self.calle} {self.altura}{departamento_str},
        {barrio_str}, CP: {self.codigo_postal}"""
    
