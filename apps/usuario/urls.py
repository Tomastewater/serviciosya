from .views import usuarioFormView, homeView, aboutView, consumidorView, direccionView, ubicacionFormView, prestadorView, contratoView, facturaView
from django.urls import path


urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('acercade/', aboutView.as_view(), name='about'),
    path('consumidor/', consumidorView.as_view(), name='consumidor'),
    path('prestador/', prestadorView.as_view(), name='prestador'),
    # path('consumidor/direcciones/', direccionView.as_view(), name='oneDirection'),
    path('consumidor/direcciones/', ubicacionFormView.as_view(), name='oneDirection'),
    path('prestador/contratos/', contratoView.as_view(), name='contratos'),
    path('prestador/facturas/', facturaView.as_view(), name='facturas'),
 
]
