from django.contrib import admin

from apps.prestador.models import Prestador
@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "codFiscal"]
