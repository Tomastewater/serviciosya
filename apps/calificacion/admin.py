from django.contrib import admin

from apps.calificacion.models import Calificacion
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    pass


