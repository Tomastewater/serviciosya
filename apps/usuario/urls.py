from .views import usuarioFormView, homeView, aboutView, ServiciosListView, ServicioDetailView, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from apps.prestador.views import PrestadorPanelView, PrestadorDireccionListView, PrestadorDatosView, PrestadorContratosListView, PrestadorFacturasListView, CalificacionesListView
from apps.consumidor.views import ConsumidorPanelView, ConsumidorDireccionListView, ConsumidorDatosView, ConsumidorContratosListView, ConsumidorPagosListView
from apps.ubicacion.views import ModificarDireccionView, EliminarDireccionView, PrestadorEliminarDireccionView, PrestadorModificarDireccionView

urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('acercade/', aboutView.as_view(), name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('servicios/', ServiciosListView.as_view(), name='servicios'),
    path('servicios/<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
    path('prestador/', PrestadorPanelView.as_view(), name='prestador'),
    path('prestador/datos/', PrestadorDatosView.as_view(), name='datos'),
    path('prestador/direcciones/', PrestadorDireccionListView.as_view(), name='direcciones'),
    path('prestador/contratos/', PrestadorContratosListView.as_view(), name='contratos'),
    path('prestador/facturas/', PrestadorFacturasListView.as_view(), name='facturas'),
    path('prestador/calificaciones/', CalificacionesListView.as_view(), name='calificaciones'),
    path('prestador/modificar_direccion/<int:direccion_id>/', PrestadorModificarDireccionView.as_view(), name='modificar_dire_prestador'),
    path('prestador/eliminar_direccion/<int:direccion_id>/', PrestadorEliminarDireccionView.as_view(), name='eliminar_dire_prestador'),
    path('consumidor/', ConsumidorPanelView.as_view(), name='consumidor'),
    path('consumidor/datos/', ConsumidorDatosView.as_view(), name='datos_consumidor'),
    path('consumidor/direcciones/', ConsumidorDireccionListView.as_view(), name='dire_consumidor'),
    path('consumidor/contratos/', ConsumidorContratosListView.as_view(), name='contratos_consumidor'),
    path('consumidor/pagos/', ConsumidorPagosListView.as_view(), name='pagos'),
    path('consumidor/modificar_direccion/<int:direccion_id>/', ModificarDireccionView.as_view(), name='modificar_direccion'),
    path('consumidor/eliminar_direccion/<int:direccion_id>/', EliminarDireccionView.as_view(), name='eliminar_direccion'),

]
