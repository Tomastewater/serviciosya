from django.db import models

class Factura(models.Model):
    fecha_emision = models.DateField()
    impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    detalles = models.TextField(max_length=500)

    def __str__(self) -> str:
        total_con_impuestos = self.monto_total + self.impuestos
        return f"Fecha: {self.fecha_emision} | Monto: ${self.monto_total} | Impuestos: ${self.impuestos} | Total (con impuestos): ${total_con_impuestos}"
