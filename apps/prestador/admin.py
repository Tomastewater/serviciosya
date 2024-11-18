from django.contrib import admin
from .models import Prestador

# Register your models here.

@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ["id", "rol_usuario", "codFiscal"]