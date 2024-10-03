from django.db import models

class Factura(models.Model):
    fecha_emision = models.DateField()
    impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    detalles = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"Fecha Emision: {self.fecha_emision} \nDetalles: {self.detalles} \nMonto del contrato: {self.monto_total} \nImpuestos: {self.impuestos} \n\nTotal + impuestos: {self.impuestos + self.monto_total}"
