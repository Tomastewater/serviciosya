from django.contrib import admin

# Register your models here.
from .models import Prestador
@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "codFiscal"]