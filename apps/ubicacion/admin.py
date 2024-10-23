from django.contrib import admin

# Register your models here.
from apps.ubicacion.models import Provincia
@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

from apps.ubicacion.models import Localidad
@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ["nombre", "provincia"]   

from apps.ubicacion.models import Direccion
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ["calle", "altura", "barrio"]    
 