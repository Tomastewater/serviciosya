from django.contrib import admin

# Register your models here.
from .models import Factura
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha_emision", "monto_total"]
    search_fields = ["id"]
    list_filter = ["fecha_emision"]