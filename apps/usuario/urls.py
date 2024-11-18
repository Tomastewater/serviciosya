from .views import usuarioFormView, homeView, aboutView, consumidorView, direccionView
from django.urls import path


urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('acercade/', aboutView.as_view(), name='about'),
    path('consumidor/', consumidorView.as_view(), name='consumidor'),
    path('consumidor/direcciones/', direccionView.as_view(), name='oneDirection')

    
]
