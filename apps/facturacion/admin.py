from django.contrib import admin

from apps.facturacion.models import Factura
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    pass
