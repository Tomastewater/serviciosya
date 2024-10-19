from django.contrib import admin

# Register your models here.
from apps.pago.models import MetodoPago
@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

from apps.pago.models import Estado
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]   

from apps.pago.models import Pago
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha_pago", "monto_pago", "estado"]