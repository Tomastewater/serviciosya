from django.contrib import admin

# Register your models here.
from apps.servicio.models import Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

from apps.servicio.models import Servicio
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "descripcion"]
    search_fields = ["nombre", "descripcion"]
    list_filter = ["categoria"]   

from apps.servicio.models import ServicioPrestado
@admin.register(ServicioPrestado)
class ServicioPrestadoAdmin(admin.ModelAdmin):
    list_display = ["prestador", "servicio", "localidad"]
    search_fields = ["localidad__nombre"]
    list_filter = ["servicio"]