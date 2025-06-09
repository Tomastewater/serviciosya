from django.db import models

class Factura(models.Model):
    """
    Modelo que representa una factura emitida por un servicio.

    Atributos:
        fecha_emision (DateField): Fecha en la que se emite la factura.
        impuestos (DecimalField): Monto correspondiente a los impuestos aplicados.
        monto_total (DecimalField): Monto total de la factura sin impuestos.
        detalles (TextField): Detalles adicionales de la factura (hasta 500 caracteres).
    """
    fecha_emision = models.DateField()
    impuestos = models.DecimalField(max_digits=15, decimal_places=2)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    detalles = models.TextField(max_length=500)

    def __str__(self) -> str:
        """
        Retorna una representación legible de la factura, mostrando fecha, monto, impuestos y total.
        """
        total_con_impuestos = self.monto_total + self.impuestos
        return f"Fecha: {self.fecha_emision} | Monto: ${self.monto_total} | Impuestos: ${self.impuestos} | Total (con impuestos): ${total_con_impuestos}"
