from django.contrib import admin

# Register your models here.
from .models import Consumidor
@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    list_display = ["id", "rol_usuario__usuario__nombre", "rol_usuario__usuario__apellido", "rol_usuario"]
    search_fields = ["rol_usuario__usuario__apellido"]
    list_filter = ["rol_usuario__usuario__fecha_creacion"]