from django.db import models

class Prestador(models.Model):
    eleccion = "prestador"

    estudios = models.TextField(max_length=500)
    codFiscal = models.CharField(max_length=100)
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} / Codigo Fiscal: {self.codFiscal}"
    
        
