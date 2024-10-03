from django.db import models

class Calificacion(models.Model):
    CALIFICACION_OPCIONES = [
        (1,'1 - Muy malo'),
        (2,'2 - Malo'),
        (3,'3 - Regular'),
        (4,'4 - Bueno'),
        (5,'5 - Excelente'),
    ]

    fecha_calificacion = models.DateField()
    Calificacion = models.IntegerField(choices=CALIFICACION_OPCIONES)
    comentario = models.TextField(max_length=1000)

    def __str__(self):
        return f"Fecha de la Calificacion: {self.fecha_calificacion} \nCalificacion: {self.Calificacion}/5 \nComentario: {self.comentario}"
    
