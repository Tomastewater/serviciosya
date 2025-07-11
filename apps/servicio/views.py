from django.shortcuts import render, redirect
from .forms import ServicioPrestadoForm
from .models import ServicioPrestado
from django.contrib import messages
from apps.prestador.models import Prestador
from apps.usuario.models import Rol
from django.http import HttpResponseForbidden


from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

def crear_servicio(request):
    """
    Vista para crear un nuevo ServicioPrestado.

    Si la petición es POST y el formulario es válido, asocia el servicio al prestador autenticado,
    guarda el servicio y redirige al panel del prestador mostrando un mensaje de éxito.
    Si la petición es GET, muestra el formulario vacío.
    """
    if request.method == 'POST':
        form = ServicioPrestadoForm(request.POST, request.FILES)
        if form.is_valid():
            servicio_prestado = form.save(commit=False)

            # Verificamos que el usuario tenga un Rol de prestador (rol=2)
            rol_prestador = Rol.objects.filter(usuario=request.user, rol=2).first()
            if not rol_prestador:
                return HttpResponseForbidden("No se encontró un rol de prestador para este usuario.")
             
             # Buscamos el objeto Prestador correspondiente al rol
            try:
                prestador = Prestador.objects.get(rol_usuario=rol_prestador)
            except Prestador.DoesNotExist:
                messages.error(request, "No se encontró un objeto Prestador asociado a este rol.")
                return redirect('prestador')
                
            servicio_prestado.prestador = prestador
            servicio_prestado.save()
            messages.success(request, "El servicio fue creado con éxito.")
            return redirect('prestador')  # vuelve al panel prestador
    else:
        form = ServicioPrestadoForm()
    return render(request, 'servicio/crear_servicio.html', {'form': form})

class ServiciosPrestadosListView(ListView):
    """
    Vista para listar los servicios ofrecidos por el prestador autenticado.
    """
    model = ServicioPrestado
    template_name = 'servicio/servicios_prestados_panel.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        """
        Filtra los servicios por el prestador autenticado.
        """
        rol_prestador = Rol.objects.get(usuario=self.request.user, rol=2)
        prestador = Prestador.objects.get(rol_usuario=rol_prestador)
        return ServicioPrestado.objects.filter(prestador=prestador)

class ServicioPrestadoUpdateView(UpdateView):
    """
    Vista para editar un servicio ofrecido por el prestador autenticado.
    Solo permite editar servicios propios.
    """
    model = ServicioPrestado
    form_class = ServicioPrestadoForm
    template_name = 'servicio/editar_servicio.html'
    success_url = reverse_lazy('servicios_prestados')

    def get_queryset(self):
        """
        Filtra los servicios por el prestador autenticado.
        """
        rol_prestador = Rol.objects.get(usuario=self.request.user, rol=2)
        prestador = Prestador.objects.get(rol_usuario=rol_prestador)
        return ServicioPrestado.objects.filter(prestador=prestador)

class ServicioPrestadoDeleteView(DeleteView):
    """
    Vista para eliminar un servicio ofrecido por el prestador autenticado.
    Solo permite eliminar servicios propios.
    """
    model = ServicioPrestado
    template_name = 'servicio/eliminar_servicio.html'
    success_url = reverse_lazy('servicios_prestados')

    def get_queryset(self):
        """
        Filtra los servicios por el prestador autenticado.
        """
        rol_prestador = Rol.objects.get(usuario=self.request.user, rol=2)
        prestador = Prestador.objects.get(rol_usuario=rol_prestador)
        return ServicioPrestado.objects.filter(prestador=prestador)
