from django.contrib import admin
from apps.pago.models import MetodoPago
from apps.pago.models import Pago

# Configuración de la administración para el modelo MetodoPago
@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo MetodoPago.

    - list_display: Muestra los campos especificados en la lista de objetos.
    """
    list_display = ["id", "nombre"]

# Configuración de la administración para el modelo Pago
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Pago.

    - list_display: Muestra los campos especificados en la lista de objetos.
    - search_fields: Permite buscar pagos por ID y estado.
    - list_filter: Permite filtrar por fecha de pago.
    """
    list_display = ["id", "fecha_pago", "monto_pago", "estado"]
    search_fields = ["id", "estado"]
    list_filter = ["fecha_pago"]