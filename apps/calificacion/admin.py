from django.contrib import admin

from .models import Calificacion

<<<<<<< HEAD
@admin.register(Calificacion)    # Los decoradores son fucniones que haran ALGO antes o despues de la clase
class calificacionAdmin(admin.ModelAdmin):
    list_display = []   # Que queremos mostrar
    search_fields = []  # lo Que queremos buscar  (Podemos buscar por los datos correspondiente a los campos)
    list_filter = []  # que queremos filtrar
=======
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    pass

>>>>>>> 9c60c0cafe35cda2fdb7483e285c4ca4445ce955

# Buscar acerca de Admin Actions