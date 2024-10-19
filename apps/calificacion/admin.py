from django.contrib import admin

from .models import Calificacion

@admin.register(Calificacion)    # Los decoradores son fucniones que haran ALGO antes o despues de la clase
class calificacionAdmin(admin.ModelAdmin):
    list_display = []   # Que queremos mostrar
    search_fields = []  # lo Que queremos buscar  (Podemos buscar por los datos correspondiente a los campos)
    list_filter = []  # que queremos filtrar

# Buscar acerca de Admin Actions