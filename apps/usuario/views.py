from django.views import generic
from .form import UsuarioForm
from apps.ubicacion.form import direccionForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Usuario, Rol
from apps.contrato.models import Contrato
from apps.ubicacion.models import Direccion
from apps.facturacion.models import Factura
from apps.prestador.models import Prestador
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class usuarioFormView(generic.FormView):
    template_name = 'formRegistrarse.html'
    form_class = UsuarioForm
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

class consumidorView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index_consumidor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el usuario autenticado
        usuario = self.request.user

        contratos = Contrato.objects.filter(direccion__usuario=usuario)  
        direcciones = Direccion.objects.filter(usuario=usuario)
        
        context['contratos'] = contratos
        context['direcciones'] = direcciones
        context['usuario'] = usuario

        return context
        
class direccionView(generic.TemplateView):
    template_name = 'directions.html'

    def get_context_data(self, **kwargs):

        usuario = self.request.user

        context =  super().get_context_data(**kwargs)
        context['direcciones'] = Direccion.objects.filter(direccion__usuario =usuario)
        context['usuarios'] = usuario
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
    
class CustomLoginView(generic.View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, autenticamos al usuario
            user = form.get_user()
            login(request, user)
            # messages.success(request, '¡Bienvenido! Has iniciado sesión correctamente.')
            return redirect(reverse_lazy('consumidor'))  # Redirige a la vista de consumidor
        else:
            # Si no es válido, mostramos un mensaje de error
            messages.error(request, 'Error en las credenciales, por favor intenta nuevamente.')
            return render(request, 'registration/login.html', {'form': form})