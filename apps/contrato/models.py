from django.db import models
from ubicacion.models import DireccionConsumidor
from servicio.models import ServicioPrestado

class Contrato(models.Model):
    fechaContrato = models.DateTimeField()
    fechaServicio = models.DateTimeField()
    precioAcordado = models.DecimalField(max_digits=20)
    estado = models.enums['En proceso', 'Cancelado', 'Completado']
    detalles = models.TextField(max_length=1000)
    direccionConsumidor = models.ForeignKey(DireccionConsumidor, on_delete=models.CASCADE)
    servicioPrestado = models.ForeignKey(ServicioPrestado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"""
        Fecha Contratacion: {self.fechaContrato}
        Fecha Servicio: {self.fechaServicio}
        Servicio Prestado: {self.servicioPrestado.servicio.nombre}
        Direccion del consumidor: {self.direccionConsumidor.direccion}
        Precio acordado por el servicioL: {self.precioAcordado}
        Estado del contrato: {self.estado}
        Detalles: {self.detalles}
        """

