from django.db import models

class Prestador(models.Model):
    eleccion = "prestador"
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, null=True)
    codFiscal = models.CharField(max_length=20)
    estudios = models.TextField(max_length=50)
    
    

    def __set__(self):
        return f"Nombre Prestador: {self.usuario.nombre} \nApellido Prestador: {self.usuario.apellido}"
    
