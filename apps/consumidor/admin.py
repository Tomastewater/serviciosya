from django.contrib import admin

# Importa el modelo Consumidor desde la aplicación actual
from .models import Consumidor

@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    
    """
    Configuración de la interfaz de administración para el modelo Consumidor.

    - list_display: Muestra los campos especificados en la lista de objetos.
    - search_fields: Permite buscar consumidores por apellido del usuario relacionado.
    - list_filter: Permite filtrar por la fecha de creación del usuario relacionado.
    """

    list_display = ["id", "rol_usuario__usuario__nombre", "rol_usuario__usuario__apellido", "rol_usuario"]
    search_fields = ["rol_usuario__usuario__apellido"]
    list_filter = ["rol_usuario__usuario__fecha_creacion"]