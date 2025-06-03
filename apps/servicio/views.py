from django.shortcuts import render, redirect
from .forms import ServicioPrestadoForm
from .models import ServicioPrestado
from django.contrib import messages
from apps.prestador.models import Prestador
from apps.usuario.models import Rol


def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioPrestadoForm(request.POST, request.FILES)
        if form.is_valid():
            servicio_prestado = form.save(commit=False)
            # Obtener el rol de prestador del usuario actual
            rol_prestador = Rol.objects.get(usuario=request.user, rol=2)
            # Obtener el objeto Prestador
            prestador = Prestador.objects.get(rol_usuario=rol_prestador)
            servicio_prestado.prestador = prestador
            servicio_prestado.save()
            messages.success(request, "El servicio fue creado con éxito.")
            return redirect('prestador')  # vuelve al panel prestador
    else:
        form = ServicioPrestadoForm()
    return render(request, 'servicio/crear_servicio.html', {'form': form})
