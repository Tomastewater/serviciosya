from django.contrib import admin

# Register your models here.
from .models import Contrato
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha_contrato", "estado", "servicio_prestado"]