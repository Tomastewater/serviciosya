from django.contrib import admin

# Register your models here.
from .models import Factura
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    pass