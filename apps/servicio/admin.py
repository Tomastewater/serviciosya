from django.contrib import admin

# Register your models here.
from apps.servicio.models import Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

from apps.servicio.models import Servicio
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria"]   

from apps.servicio.models import ServicioPrestado
@admin.register(ServicioPrestado)
class ServicioPrestadoAdmin(admin.ModelAdmin):
    list_display = ["prestador", "servicio", "barrio"]