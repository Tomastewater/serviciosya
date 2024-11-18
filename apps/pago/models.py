from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
class Pago(models.Model):
    ESTADO_PAGO = [
        (1, 'En proceso'),
        (2, 'Cancelado'),
        (3, 'Completado'),
    ]

    contrato = models.ForeignKey("contrato.Contrato", on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto_pago = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADO_PAGO)
    detalles = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f"Contrato: #{self.contrato.id} | Fecha del pago: {self.fecha_pago} | Monto: {self.monto_pago} | Método: {self.metodo_pago} | Estado: {self.estado}"