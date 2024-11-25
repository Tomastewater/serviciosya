from django.contrib import admin

# Register your models here.
from apps.ubicacion.models import Provincia
@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

from apps.ubicacion.models import Localidad
@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ["nombre", "provincia__nombre"]   

from apps.ubicacion.models import Direccion
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ["calle", "altura", "barrio", "localidad", "usuario__apellido", "usuario__nombre"]
    search_fields = ["barrio"]    
 