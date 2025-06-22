from django.db import models

class Contrato(models.Model):
    ESTADO_OPCIONES = [
        (1, 'En proceso'),
        (2, 'Cancelado'),
        (3, 'Completado'),
    ]

    fecha_contrato = models.DateTimeField()
    fecha_servicio = models.DateTimeField()
    precio_acordado = models.DecimalField(max_digits=20, decimal_places=2)
    estado = models.IntegerField(choices=ESTADO_OPCIONES)
    detalles = models.TextField(max_length=1000, null=True, blank=True)
    direccion = models.ForeignKey("ubicacion.Direccion", on_delete=models.CASCADE, default=None)
    servicio_prestado = models.ForeignKey("servicio.ServicioPrestado", on_delete=models.CASCADE)
    factura = models.ForeignKey("facturacion.Factura", on_delete=models.CASCADE, null=True, blank=True, related_name="contratos")
    consumidor = models.ForeignKey("consumidor.Consumidor", on_delete=models.CASCADE, null=True, blank=True, related_name="contratos")

    def __str__(self) -> str:

        return f"Contrato #{self.id} | Fecha: {self.fecha_contrato.strftime('%d/%m/%Y %H:%M')} | {self.servicio_prestado.servicio.nombre} | Dirección {self.direccion.calle} {self.direccion.altura} | Precio: ${self.precio_acordado} | Estado: {self.estado}"

class SolicitudServicio(models.Model):
    ESTADO_SOLICITUD = [
        (1, 'Pendiente'),
        (2, 'Aceptada'),
        (3, 'Rechazada'),
    ]

    consumidor = models.ForeignKey("consumidor.Consumidor", on_delete=models.CASCADE)
    servicio_prestado = models.ForeignKey("servicio.ServicioPrestado", on_delete=models.CASCADE)
    direccion = models.ForeignKey("ubicacion.Direccion", on_delete=models.CASCADE)
    fecha_solicitada = models.DateTimeField()
    estado = models.IntegerField(choices=ESTADO_SOLICITUD, default=1)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud #{self.id} - {self.servicio_prestado} - {self.get_estado_display()}"
