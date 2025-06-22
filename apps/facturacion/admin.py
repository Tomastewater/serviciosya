from django.contrib import admin

# Importa el modelo Factura desde la aplicación actual
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Factura.

    - list_display: Muestra los campos especificados en la lista de objetos.
    - search_fields: Permite buscar facturas por ID.
    - list_filter: Permite filtrar por fecha de emisión.
    """
    list_display = ["id", "fecha_emision", "monto_total"]
    search_fields = ["id"]
    list_filter = ["fecha_emision"]