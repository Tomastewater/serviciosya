from .views import usuarioFormView, homeView, aboutView, ServiciosListView, ServicioDetailView, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from apps.prestador.views import PrestadorPanelView, PrestadorDireccionListView, PrestadorDatosView, PrestadorContratosListView, PrestadorFacturasListView, CalificacionesListView
from apps.consumidor.views import ConsumidorPanelView, ConsumidorDireccionListView, ConsumidorDatosView, ConsumidorContratosListView, ConsumidorPagosListView, ModificarDireccionView, EliminarDireccionView
from apps.ubicacion.views import PrestadorEliminarDireccionView, PrestadorModificarDireccionView
from apps.servicio.views import crear_servicio, ServiciosPrestadosListView, ServicioPrestadoUpdateView, ServicioPrestadoDeleteView
from apps.contrato.views import solicitar_servicio, solicitudes_prestador, aceptar_solicitud
from apps.contrato.views import actualizar_estado_contrato

from apps.contrato.views import todas_las_solicitudes


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
    path('prestador/contratos/', PrestadorContratosListView.as_view(), name='contratos_prestador'),
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
    path('prestador/servicio/nuevo/', crear_servicio, name='crear_servicio'),
    path('prestador/servicios/', ServiciosPrestadosListView.as_view(), name='servicios_prestados'),
    path('prestador/servicio/<int:pk>/editar/', ServicioPrestadoUpdateView.as_view(), name='editar_servicio'),
    path('prestador/servicio/<int:pk>/eliminar/', ServicioPrestadoDeleteView.as_view(), name='eliminar_servicio'),
    path('solicitar_servicio/<int:servicio_id>/', solicitar_servicio, name='solicitar_servicio'),
    path('prestador/solicitudes/', solicitudes_prestador, name='solicitudes_prestador'),
    path('prestador/solicitudes/aceptar/<int:solicitud_id>/', aceptar_solicitud, name='aceptar_solicitud'),
    path('prestador/contrato/<int:contrato_id>/actualizar_estado/', actualizar_estado_contrato, name='actualizar_estado'),
    # comprobando que las solicitudes de servicio se hagan correctamente
    path('debug/todas_solicitudes/', todas_las_solicitudes, name='todas_solicitudes'),


]
