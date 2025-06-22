from django.contrib import admin
from apps.ubicacion.models import Provincia

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Provincia.

    - list_display: Muestra los campos especificados en la lista de objetos.
    """
    list_display = ["id", "nombre"]

from apps.ubicacion.models import Localidad
@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Localidad.

    - list_display: Muestra el nombre de la localidad y el nombre de la provincia asociada.
    """
    list_display = ["nombre", "provincia__nombre"]   

from apps.ubicacion.models import Direccion
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo Direccion.

    - list_display: Muestra los campos especificados en la lista de objetos.
    - search_fields: Permite buscar direcciones por barrio.
    """
    list_display = ["calle", "altura", "barrio", "localidad", "usuario__apellido", "usuario__nombre"]
    search_fields = ["barrio"]
