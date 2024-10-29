from .views import usuarioFormView
from django.urls import path

urlpatterns = [
    path('agregar_usuario/', usuarioFormView.as_view(), name='add_user'),
]
