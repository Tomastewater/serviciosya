from .views import usuarioFormView
from django.urls import path


urlpatterns = [
    path('agregarUsuario/', usuarioFormView.as_view(), name='add_user'),
    
]
