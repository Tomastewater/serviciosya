from django.db import models

class Contrato(models.Model):
    ESTADO_OPCIONES = [
        ('en_proceso', 'En proceso'),
        ('cancelado', 'Cancelado'),
        ('completado', 'Completado'),
    ]

    fecha_contrato = models.DateTimeField()
    fecha_servicio = models.DateTimeField()
    precio_acordado = models.DecimalField(max_digits=20, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES)
    detalles = models.TextField(max_length=1000)
    direccion = models.ForeignKey("ubicacion.Direccion", on_delete=models.CASCADE, default=None)
    servicio_prestado = models.ForeignKey("servicio.ServicioPrestado", on_delete=models.CASCADE)
    factura = models.ForeignKey("facturacion.Factura", on_delete=models.CASCADE, null=True, blank=True, related_name="contratos")

    def __str__(self) -> str:

        return f"Contrato #{self.id} | Fecha: {self.fecha_contrato.strftime('%d/%m/%Y %H:%M')} | {self.servicio_prestado.servicio.nombre} | Dirección {self.direccion.calle} {self.direccion.altura} | Precio: ${self.precio_acordado} | Estado: {self.estado}"


"""
        Fecha Contratacion: {self.fecha_contrato}
        Fecha Servicio: {self.fecha_servicio}
        Servicio Prestado: {self.servicio_prestado.servicio.nombre}
        Direccion del consumidor: {self.direccion_consumidor.direccion.barrio}, {self.direccion_consumidor.direccion.calle}, {self.direccion_consumidor.direccion.altura}
        Precio acordado por el servicioL: {self.precio_acordado}
        Estado del contrato: {self.estado}
        Detalles: {self.detalles}
        """