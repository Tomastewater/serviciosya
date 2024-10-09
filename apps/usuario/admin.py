from django.contrib import admin

from apps.usuario.models import Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "email"]
    search_fields = ["apellido"]
