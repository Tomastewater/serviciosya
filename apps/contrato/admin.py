from django.contrib import admin

from apps.contrato.models import Contrato
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha_contrato", "estado", "servicio_prestado"]
