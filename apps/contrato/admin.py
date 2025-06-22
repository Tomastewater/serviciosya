from django.contrib import admin

# Importa el modelo Contrato desde la aplicación actual
from .models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Contrato.

    - list_display: Muestra los campos especificados en la lista de objetos.
    - search_fields: Permite buscar contratos por estado.
    - list_filter: Permite filtrar por fecha de contrato y fecha de servicio.
    """
    list_display = ["fecha_contrato", "estado", "servicio_prestado", "factura__monto_total"]
    search_fields = ["estado"]
    list_filter = ["fecha_contrato", "fecha_servicio"]

