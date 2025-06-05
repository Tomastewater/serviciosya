from django.views import generic
from django.urls import reverse_lazy
from .models import Rol
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .form import UsuarioForm
from apps.servicio.models import Servicio, Categoria, ServicioPrestado
from apps.ubicacion.models import Localidad


class usuarioFormView(generic.FormView):
    template_name = 'formRegistrarse.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class registerView(generic.TemplateView):
    template_name = 'register.html'

class homeView(generic.TemplateView):
    template_name = 'home.html'

class aboutView(generic.TemplateView):
    template_name = 'about.html'

class CustomLoginView(generic.View):

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # Si el formulario es válido, autenticamos al usuario
            usuario = form.get_user()
            login(request, usuario)
            
            # Determinar el rol del usuario
            try:
                rol_usuario = usuario.roles.first()  # Obtener el primer rol asociado al usuario
                if rol_usuario.rol == 1:  # Consumidor
                    return redirect(reverse_lazy('consumidor'))
                elif rol_usuario.rol == 2:  # Prestador
                    return redirect(reverse_lazy('prestador'))
            except Rol.DoesNotExist:
                messages.error(request, 'No se encontró un rol asociado al usuario.')
                return redirect(reverse_lazy('login'))  # Redirige al login en caso de error

        else:
            # Si no es válido, mostramos un mensaje de error
            messages.error(request, 'Error en las credenciales, por favor intenta nuevamente.')
            return render(request, 'registration/login.html', {'form': form})

class servicesView(generic.TemplateView):
    template_name = 'lista_de_servicios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categorias'] = Categoria.objects.all()
        categoria_id = self.request.GET.get('categoria', None)

        if categoria_id:
            context['servicios'] = Servicio.objects.filter(categoria_id=categoria_id).order_by('nombre')
        else:
            context['servicios'] = Servicio.objects.order_by('nombre')
        return context
    
class ServiciosListView(generic.ListView):
    model = ServicioPrestado
    template_name = 'lista_de_servicios.html'
    context_object_name = 'servicios'
    
    def get_queryset(self):
        queryset = ServicioPrestado.objects.select_related('prestador', 'categoria', 'localidad')
        categoria_id = self.request.GET.get('categoria')
        localidad_id = self.request.GET.get('localidad')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        if localidad_id:
            queryset = queryset.filter(localidad_id=localidad_id)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['localidades'] = Localidad.objects.all()
        context['categoria_id'] = self.request.GET.get('categoria', '')
        context['localidad_id'] = self.request.GET.get('localidad', '')
        return context


class ServicioDetailView(generic.DetailView):
    template_name = 'servicio_detail.html'
    model = Servicio
    context_object_name = 'servicioPrestado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtén los servicios prestados relacionados con este servicio
        context['prestadores'] = ServicioPrestado.objects.select_related(
            'prestador', 'localidad', 'servicio'
        ).filter(servicio=self.object)
        return context
        