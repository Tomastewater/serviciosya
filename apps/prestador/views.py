from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from apps.contrato.models import Contrato
from apps.servicio.models import ServicioPrestado
from apps.facturacion.models import Factura
from apps.prestador.models import Prestador
from apps.calificacion.models import Calificacion

class PrestadorPanelView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'prestador_panel.html'

    def get_context_data(self, **kwargs):

        usuario_actual = self.request.user

        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context


class PrestadorDatosView(generic.TemplateView):
    template_name = 'prestador_datos_personales.html'

    def get_context_data(self, **kwargs):

        usuario_actual = self.request.user
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()

        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        context['prestador'] = prestador
        return context

class PrestadorDireccionListView(generic.ListView):
    model = ServicioPrestado
    template_name = 'prestador_direcciones.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        usuario_actual = self.request.user
        prestador = Prestador.objects.get(rol_usuario__usuario=usuario_actual)  # Obtiene el prestador del usuario actual
        return ServicioPrestado.objects.filter(prestador=prestador)
    
    

class PrestadorFacturasListView(generic.ListView):
    model = Factura
    template_name = "prestador_facturas.html"
    context_object_name = "facturas"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        # Obtener el prestador asociado al usuario
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()

        # Filtrar facturas relacionadas con los contratos del prestador
        return Factura.objects.filter(contratos__servicio_prestado__prestador=prestador)

class PrestadorContratosListView(generic.ListView):
    model = Contrato
    template_name = "prestador_contratos.html"
    context_object_name = "contratos"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        # Obtener el prestador asociado al usuario
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()
        
        if prestador:
            # Filtrar contratos del prestador
            return Contrato.objects.filter(servicio_prestado__prestador=prestador)
        return Contrato.objects.none() 

class CalificacionesListView(generic.ListView):
    model = Calificacion
    template_name = "calificaciones.html"
    context_object_name = "calificaciones"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        return Calificacion.objects.filter(prestador__rol_usuario__usuario=usuario_actual)