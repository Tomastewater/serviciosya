from django.shortcuts import render, redirect
from .forms import ServicioPrestadoForm
from .models import ServicioPrestado

def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioPrestadoForm(request.POST, request.FILES)
        if form.is_valid():
            servicio_prestado = form.save(commit=False)
            servicio_prestado.prestador = request.user.rol_usuario.prestador
            servicio_prestado.save()
            return redirect('prestador_panel')  # Cambiá esto por la URL que uses para volver al panel
    else:
        form = ServicioPrestadoForm()
    return render(request, 'servicio/crear_servicio.html', {'form': form})
