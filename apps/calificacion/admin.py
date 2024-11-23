from django.contrib import admin

from .models import Calificacion

@admin.register(Calificacion)    # Los decoradores son fucniones que haran ALGO antes o despues de la clase
class calificacionAdmin(admin.ModelAdmin):
    list_display = ["fecha_calificacion", "calificacion","prestador"]  # Que queremos mostrar
    search_fields = ["calificacion"]  # lo Que queremos buscar  (Podemos buscar por los datos correspondiente a los campos)
    list_filter = ["fecha_calificacion"]  # que queremos filtrar

# Buscar acerca de Admin Actions


