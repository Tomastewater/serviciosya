from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from apps.contrato.models import Contrato
from apps.servicio.models import ServicioPrestado
from apps.facturacion.models import Factura
from apps.prestador.models import Prestador
from apps.calificacion.models import Calificacion
from apps.ubicacion.models import Direccion, Localidad, Provincia
from apps.ubicacion.form import DireccionForm

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
    

class PrestadorDireccionListView(generic.ListView, generic.edit.FormMixin):
    model = Direccion
    template_name = 'prestador_direcciones.html'
    context_object_name = 'direcciones'
    form_class = DireccionForm

    def get_queryset(self):
        usuario_actual = self.request.user
        return Direccion.objects.filter(usuario=usuario_actual)

    def get_context_data(self, **kwargs):
        # Agrega el formulario al contexto de la plantilla
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Incluye el formulario en el contexto
        return context
    
    def post(self, request, *args, **kwargs):
        # Manejo del formulario al enviarse
        form = self.get_form()
        if form.is_valid():
            nueva_direccion = form.save(commit=False)
            nueva_direccion.usuario = self.request.user  # Asocia la dirección al usuario logueado
            nueva_direccion.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Redirige a la misma página después de guardar la dirección
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la misma página
        return reverse_lazy('direcciones')    


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