from django.db import models

class Prestador(models.Model):

    estudios = models.TextField(max_length=500, null=True, blank=True)
    codFiscal = models.CharField(max_length=100, null=True, blank=True)
    CUIT = models.CharField(max_length=100, null=True, blank=True)
    rol_usuario = models.ForeignKey("usuario.Rol", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        nombre_completo = f"{self.rol_usuario.usuario.nombre} {self.rol_usuario.usuario.apellido}"
        return f"{nombre_completo} | CUIT: {self.CUIT}"
    
        
