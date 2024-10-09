from django.contrib import admin

from apps.consumidor.models import Consumidor
@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario"]