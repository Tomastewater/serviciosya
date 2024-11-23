from django.views import generic
from .form import usuarioForm
from apps.ubicacion.form import direccionForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Usuario, Rol
from apps.contrato.models import Contrato
from apps.ubicacion.models import Direccion
from apps.facturacion.models import Factura
from apps.prestador.models import Prestador


class usuarioFormView(generic.FormView):
    template_name = 'formRegistrarse.html'
    form_class = usuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ubicacionFormView(generic.FormView):
    template_name = 'formUbicacion.html'
    form_class = direccionForm
    success_url = reverse_lazy('oneDirection')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class registerView(generic.TemplateView):
    template_name = 'register.html'

class homeView(generic.TemplateView):
    template_name = 'home.html'

class aboutView(generic.TemplateView):
    template_name = 'about.html'

class consumidorView(generic.TemplateView):
    template_name = 'index_consumidor.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['contratos'] = Contrato.objects.all()
        context['usuarios'] = Usuario.objects.all()
        return context
        
class direccionView(generic.TemplateView):
    template_name = 'directions.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['direcciones'] = Direccion.objects.all()
        context['usuarios'] = Usuario.objects.all()
        return context

class PrestadorView(generic.TemplateView):
    template_name = 'index_prestador.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['prestador'] = Prestador.objects.get(id=3)
        context['usuarios'] = Usuario.objects.all()
        return context

class PrestadorPanelView(generic.TemplateView):
    template_name = 'prestador_panel.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['prestador'] = Prestador.objects.get(id=3)
        context['usuarios'] = Usuario.objects.all()
        return context

class PrestadorDatosView(generic.TemplateView):
    template_name = 'prestador_datos_personales.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['prestador'] = Prestador.objects.get(id=3)
        return context

class PrestadorDireccionView(generic.TemplateView):
    template_name = 'prestador_direcciones.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['direcciones'] = Direccion.objects.all().filter(usuario_id=44)
        context["prestador"] = Prestador.objects.get(id=3)
        return context 

class PrestadorFacturaView(generic.TemplateView):
    template_name = 'prestador_facturas.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['contratos'] = Contrato.objects.all().filter(servicio_prestado__prestador=3)
        context["prestador"] = Prestador.objects.get(id=3)
        context['facturas'] = Factura.objects.filter(contratos__servicio_prestado__prestador__id=3)
        return context 

class PrestadorContratoView(generic.TemplateView):
    template_name = 'prestador_contratos.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['contratos'] = Contrato.objects.all().filter(servicio_prestado__prestador=3)
        context['prestador'] = Prestador.objects.get(id=3)
        return context