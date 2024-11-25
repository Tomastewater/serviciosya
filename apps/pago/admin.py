from django.contrib import admin
from apps.pago.models import MetodoPago
from apps.pago.models import Pago

# Register your models here.

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha_pago", "monto_pago", "estado"]
    search_fields = ["id", "estado"]
    list_filter = ["fecha_pago"]