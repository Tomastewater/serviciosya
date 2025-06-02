from django.shortcuts import render, redirect
from .forms import ServicioPrestadoForm
from .models import ServicioPrestado
from django.contrib import messages


def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioPrestadoForm(request.POST, request.FILES)
        if form.is_valid():
            servicio_prestado = form.save(commit=False)
            servicio_prestado.prestador = request.user.rol_usuario.prestador
            servicio_prestado.save()
            messages.success(request, "El servicio fue creado con éxito.")
            return redirect('prestador_panel')  # vuelve al panel prestador
    else:
        form = ServicioPrestadoForm()
    return render(request, 'servicio/crear_servicio.html', {'form': form})
