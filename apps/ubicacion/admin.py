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

from apps.ubicacion.models import Barrio
@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "localidad"]

from apps.ubicacion.models import Direccion
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ["calle", "altura", "barrio"]    

from apps.ubicacion.models import DireccionConsumidor
@admin.register(DireccionConsumidor)
class DireccionConsumidorAdmin(admin.ModelAdmin):
    list_display = ["direccion", "consumidor"]     