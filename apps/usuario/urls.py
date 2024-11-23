from .views import usuarioFormView, homeView, aboutView, consumidorView, direccionView, ubicacionFormView, PrestadorPanelView, PrestadorDireccionView, PrestadorDatosView, PrestadorContratoView, PrestadorFacturaView, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('acercade/', aboutView.as_view(), name='about'),
    path('consumidor/', consumidorView.as_view(), name='consumidor'),
    path('prestador/', PrestadorPanelView.as_view(), name='panel'),
    # path('prestador/panel/', PrestadorPanelView.as_view(), name='panel'),
    path('prestador/datos/', PrestadorDatosView.as_view(), name='datos'),
    path('prestador/direcciones/', PrestadorDireccionView.as_view(), name='direcciones'),
    # path('consumidor/direcciones/', direccionView.as_view(), name='oneDirection'),
    path('consumidor/direcciones/', ubicacionFormView.as_view(), name='oneDirection'),
    path('prestador/contratos/', PrestadorContratoView.as_view(), name='contratos'),
    path('prestador/facturas/', PrestadorFacturaView.as_view(), name='facturas'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
 
]
