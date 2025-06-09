from django.db import models

class Calificacion(models.Model):
    """
    Modelo que representa una calificación realizada por un usuario a un prestador de servicios.

    Atributos:
        fecha_calificacion (DateField): Fecha en la que se realizó la calificación.
        calificacion (IntegerField): Valor numérico de la calificación, de 1 (Muy malo) a 5 (Excelente).
        comentario (TextField): Comentario adicional sobre la calificación, hasta 1000 caracteres.
        prestador (ForeignKey): Referencia al prestador calificado.
    """

    CALIFICACION_OPCIONES = [
        (1,'1 - Muy malo'),
        (2,'2 - Malo'),
        (3,'3 - Regular'),
        (4,'4 - Bueno'),
        (5,'5 - Excelente'),
    ]

    fecha_calificacion = models.DateField()
    calificacion = models.IntegerField(choices=CALIFICACION_OPCIONES)
    comentario = models.TextField(max_length=1000)
    prestador = models.ForeignKey("prestador.Prestador", on_delete=models.CASCADE, null=True, blank=True, related_name="calificaciones")

    def __str__(self):
        return f"Fecha de la Calificacion: {self.fecha_calificacion} \nCalificacion: {self.calificacion}/5 \nComentario: {self.comentario}"
    
