from django.db import models
from usuario.models import Usuario

class Prestador(models.Model):
    eleccion = "prestador"

    estudios = models.TextField(max_length=500)
    codFiscal = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __set__(self):
        return f"Nombre Prestador: {self.usuario.nombre} \nCodigo Fiscal: {self.codFiscal}"
    
