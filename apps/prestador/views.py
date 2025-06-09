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
    """
    Vista para mostrar el panel principal del prestador.
    Requiere que el usuario esté autenticado.
    """
    template_name = 'prestador_panel.html'

    def get_context_data(self, **kwargs):
        """
        Agrega el usuario actual al contexto de la plantilla.
        """
        usuario_actual = self.request.user
        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context

class PrestadorDatosView(generic.TemplateView):
    """
    Vista para mostrar los datos personales del prestador.
    """
    template_name = 'prestador_datos_personales.html'

    def get_context_data(self, **kwargs):
        """
        Agrega el usuario y el objeto prestador al contexto de la plantilla.
        """
        usuario_actual = self.request.user
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()
        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        context['prestador'] = prestador
        return context

class PrestadorDireccionListView(generic.ListView, generic.edit.FormMixin):
    """
    Vista para listar y agregar direcciones del prestador.
    Permite mostrar las direcciones y agregar nuevas mediante un formulario.
    """
    model = Direccion
    template_name = 'prestador_direcciones.html'
    context_object_name = 'direcciones'
    form_class = DireccionForm

    def get_queryset(self):
        """
        Filtra las direcciones por el usuario autenticado.
        """
        usuario_actual = self.request.user
        return Direccion.objects.filter(usuario=usuario_actual)

    def get_context_data(self, **kwargs):
        """
        Agrega el formulario al contexto de la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        """
        Maneja el envío del formulario para agregar una nueva dirección.
        """
        form = self.get_form()
        if form.is_valid():
            nueva_direccion = form.save(commit=False)
            nueva_direccion.usuario = self.request.user
            nueva_direccion.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Redirige a la misma página después de guardar la dirección.
        """
        return super().form_valid(form)

    def get_success_url(self):
        """
        Define la URL de redirección tras agregar una dirección.
        """
        return reverse_lazy('direcciones')    

class PrestadorFacturasListView(generic.ListView):
    """
    Vista para listar las facturas asociadas a los contratos del prestador.
    """
    model = Factura
    template_name = "prestador_facturas.html"
    context_object_name = "facturas"

    def get_queryset(self):
        """
        Filtra las facturas por los contratos del prestador autenticado.
        """
        usuario_actual = self.request.user
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()
        return Factura.objects.filter(contratos__servicio_prestado__prestador=prestador)

class PrestadorContratosListView(generic.ListView):
    """
    Vista para listar los contratos asociados al prestador.
    """
    model = Contrato
    template_name = "prestador_contratos.html"
    context_object_name = "contratos"

    def get_queryset(self):
        """
        Filtra los contratos por el prestador autenticado.
        """
        usuario_actual = self.request.user
        prestador = Prestador.objects.filter(rol_usuario__usuario=usuario_actual).first()
        if prestador:
            return Contrato.objects.filter(servicio_prestado__prestador=prestador)
        return Contrato.objects.none() 

class CalificacionesListView(generic.ListView):
    """
    Vista para listar las calificaciones recibidas por el prestador.
    """
    model = Calificacion
    template_name = "calificaciones.html"
    context_object_name = "calificaciones"

    def get_queryset(self):
        """
        Filtra las calificaciones por el prestador autenticado.
        """
        usuario_actual = self.request.user
        return Calificacion.objects.filter(prestador__rol_usuario__usuario=usuario_actual)