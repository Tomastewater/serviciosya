from django.db import models

class Consumidor(models.Model):
    rol_usuario = models.ForeignKey('usuario.Rol', on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Devuelve una representación en cadena (string) de la instancia del modelo Consumidor.

        Si el consumidor tiene un usuario asociado, devuelve el nombre completo del usuario (nombre y apellido).
        Si el consumidor no tiene un usuario asociado, devuelve un mensaje indicando que no hay usuario asociado.
        """
        if self.rol_usuario:
            return f'{self.rol_usuario.usuario.nombre} {self.rol_usuario.usuario.apellido}'
        return 'Consumidor sin usuario asociado'