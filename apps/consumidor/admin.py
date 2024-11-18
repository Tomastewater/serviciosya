from django.contrib import admin

# Register your models here.
from .models import Consumidor
@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    list_display = ["id", "rol_usuario"]