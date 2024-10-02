from django.db import models
from contrato.models import Contrato 

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"Metodo de pago: {self.nombre} \nDetalle: {self.detalle}"
    
class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=500)

    def __str__(self):
        return f"Estado del pago: {self.nombre} \nDetalles: {self.detalle}"
    

class Pago(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto_pago = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    detalles = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f"Contrato: {self.contrato.id} \nFecha del pago: {self.fecha_pago} \nMonto pagado: {self.monto_pago} \nMetodo de pago: {self.metodo_pago.nombre} \nEstado del pago: {self.estado.nombre} \nDetalles del pago: {self.detalles}"