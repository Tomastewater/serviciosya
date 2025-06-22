from django.db import models

class MetodoPago(models.Model):
    """
    Modelo que representa un método de pago disponible.

    Atributos:
        nombre (CharField): Nombre del método de pago.
        detalle (TextField): Detalles adicionales sobre el método de pago (opcional).
    """
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        """
        Retorna el nombre del método de pago.
        """
        return self.nombre
    
class Pago(models.Model):
    """
    Modelo que representa un pago realizado por un consumidor.

    Atributos:
        contrato (ForeignKey): Contrato asociado al pago.
        fecha_pago (DateField): Fecha en la que se realizó el pago.
        monto_pago (DecimalField): Monto pagado.
        metodo_pago (ForeignKey): Método de pago utilizado.
        estado (IntegerField): Estado actual del pago (En proceso, Cancelado, Completado).
        detalles (TextField): Detalles adicionales sobre el pago.
    """
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
        """
        Retorna una representación legible del pago, mostrando contrato, fecha, monto, método y estado.
        """
        return f"Contrato: #{self.contrato.id} | Fecha del pago: {self.fecha_pago} | Monto: {self.monto_pago} | Método: {self.metodo_pago} | Estado: {self.estado}"