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
from django.views.generic import TemplateView

class usuarioFormView(generic.FormView):
    """
    Vista para el registro de nuevos usuarios mediante un formulario.
    """
    template_name = 'formRegistrarse.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        Guarda el usuario si el formulario es válido.
        """
        form.save()
        return super().form_valid(form)
    
class registerView(generic.TemplateView):
    """
    Vista para mostrar la página de registro.
    """
    template_name = 'register.html'

class homeView(generic.TemplateView):
    """
    Vista para mostrar la página de inicio.
    """
    template_name = 'home.html'

class aboutView(generic.TemplateView):
    """
    Vista para mostrar la página 'Acerca de'.
    """
    template_name = 'about.html'

class CustomLoginView(generic.View):
    """
    Vista personalizada para el inicio de sesión de usuarios.
    Permite autenticar y redirigir según el rol del usuario.
    """

    def get(self, request, *args, **kwargs):
        """
        Muestra el formulario de inicio de sesión.
        """
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Procesa el formulario de inicio de sesión.
        Si las credenciales son válidas, autentica y redirige según el rol.
        """
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

    
class ServiciosListView(generic.ListView):
    """
    Vista para listar los servicios prestados, con filtros por categoría y localidad.
    """
    model = ServicioPrestado
    template_name = 'lista_de_servicios.html'
    context_object_name = 'servicios'
    
    def get_queryset(self):
        """
        Filtra los servicios prestados por categoría y localidad si se especifican.
        """
        queryset = ServicioPrestado.objects.select_related('prestador', 'categoria', 'localidad')
        categoria_id = self.request.GET.get('categoria')
        localidad_id = self.request.GET.get('localidad')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        if localidad_id:
            queryset = queryset.filter(localidad_id=localidad_id)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Agrega las categorías y localidades al contexto para los filtros.
        """
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['localidades'] = Localidad.objects.all()
        context['categoria_id'] = self.request.GET.get('categoria', '')
        context['localidad_id'] = self.request.GET.get('localidad', '')

        if self.request.user.is_authenticated:
            roles = self.request.user.roles.all()
            context['rol'] = roles[0].rol if roles else None
        else:
            context['rol'] = None

        return context

class ServicioDetailView(generic.DetailView):
    """
    Vista para mostrar el detalle de un servicio específico y sus prestadores asociados.
    """
    template_name = 'servicio_detail.html'
    model = Servicio
    context_object_name = 'servicioPrestado'

    def get_context_data(self, **kwargs):
        """
        Agrega los prestadores relacionados con el servicio al contexto.
        """
        context = super().get_context_data(**kwargs)
        # Obtén los servicios prestados relacionados con este servicio
        context['prestadores'] = ServicioPrestado.objects.select_related(
            'prestador', 'localidad', 'servicio'
        ).filter(servicio=self.object)
        return context

class MantenimientoView(TemplateView):
    """
    Vista para mostrar la página de mantenimiento.
    """
    template_name = 'mantenimiento.html'
