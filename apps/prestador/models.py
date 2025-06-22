from django.db import models

class Prestador(models.Model):
    """
    Modelo que representa a un prestador de servicios.

    Atributos:
        estudios (TextField): Estudios o formación académica del prestador (opcional).
        codFiscal (CharField): Código fiscal del prestador (opcional).
        CUIT (CharField): CUIT del prestador (opcional).
        rol_usuario (ForeignKey): Referencia al rol de usuario asociado al prestador.
    """
    estudios = models.TextField(max_length=500, null=True, blank=True)
    codFiscal = models.CharField(max_length=100, null=True, blank=True)
    CUIT = models.CharField(max_length=100, null=True, blank=True)
    rol_usuario = models.ForeignKey("usuario.Rol", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """
        Retorna una representación legible del prestador, mostrando nombre completo y CUIT.
        """
        nombre_completo = f"{self.rol_usuario.usuario.nombre} {self.rol_usuario.usuario.apellido}"
        return f"{nombre_completo} | CUIT: {self.CUIT}"


