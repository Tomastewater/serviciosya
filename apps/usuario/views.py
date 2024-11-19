from django.views import generic
from .form import usuarioForm
from apps.ubicacion.form import direccionForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Usuario, Rol
from apps.contrato.models import Contrato
from apps.ubicacion.models import Direccion

class usuarioFormView(generic.FormView):
    template_name = 'formRegistrarse.html'
    form_class = usuarioForm
    success_url = reverse_lazy('register')

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