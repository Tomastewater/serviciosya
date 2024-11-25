from django.contrib import admin

# Register your models here.
from .models import Contrato
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["fecha_contrato", "estado", "servicio_prestado", "factura__monto_total"]
    search_fields = ["estado"]
    list_filter = ["fecha_contrato", "fecha_servicio"]