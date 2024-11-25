from django.contrib import admin
from .models import Prestador

# Register your models here.

@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ["id", "rol_usuario__usuario__nombre", "rol_usuario__usuario__apellido", "CUIT"]
    search_fields = ["rol_usuario__usuario__apellido"]
    list_filter = ["rol_usuario__usuario__fecha_creacion"]