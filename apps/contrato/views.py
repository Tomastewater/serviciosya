from django.shortcuts import render
from .models import SolicitudServicio
from .forms import SolicitudServicioForm
from apps.servicio.models import ServicioPrestado
from apps.consumidor.models import Consumidor
from django.utils.timezone import now
from apps.prestador.models import Prestador
from apps.facturacion.models import Factura
from .models import Contrato
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from apps.contrato.models import SolicitudServicio



@login_required
def solicitar_servicio(request, servicio_id):
    servicio = get_object_or_404(ServicioPrestado, id=servicio_id)
    consumidor = Consumidor.objects.get(rol_usuario__usuario=request.user)

    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, usuario=request.user)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.consumidor = consumidor
            solicitud.servicio_prestado = servicio
            solicitud.save()
            return redirect('contratos_consumidor')  # temporal
    else:
        form = SolicitudServicioForm(usuario=request.user)

    return render(request, 'consumidor/solicitar_servicio.html', {
        'form': form,
        'servicio': servicio
    })


@login_required
def solicitudes_prestador(request):
    prestador = Prestador.objects.get(rol_usuario__usuario=request.user)
    solicitudes = SolicitudServicio.objects.filter(servicio_prestado__prestador=prestador, estado=1)
    return render(request, 'contrato/solicitudes_prestador.html', {'solicitudes': solicitudes})


@login_required
def aceptar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudServicio, id=solicitud_id)
    solicitud.estado = 2  # Aceptada
    solicitud.save()

    contrato = Contrato.objects.create(
        consumidor=solicitud.consumidor,
        servicio_prestado=solicitud.servicio_prestado,
        direccion=solicitud.direccion,
        fecha_contrato=now(),
        fecha_servicio=solicitud.fecha_solicitada,
        precio_acordado=solicitud.servicio_prestado.precio,
        estado=1  # En proceso
    )

    # Generar factura a futuro 

    return redirect('solicitudes_prestador')


# vista para verificar que las solicitudes se hagen correctamente 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from apps.contrato.models import SolicitudServicio

@staff_member_required  # solo superusuario puede ver esto 
def todas_las_solicitudes(request):
    solicitudes = SolicitudServicio.objects.all().order_by('-fecha_solicitud')
    return render(request, 'contrato/todas_las_solicitudes.html', {
        'solicitudes': solicitudes
    })

# actualizar el estado del contrato
@login_required
def actualizar_estado_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')

        if nuevo_estado and int(nuevo_estado) in dict(Contrato.ESTADO_OPCIONES):
            contrato.estado = int(nuevo_estado)

            # Si el nuevo estado es "Completado" y aún no hay factura
            if contrato.estado == 3 and not contrato.factura:
                factura = Factura.objects.create(
                    prestador=contrato.servicio_prestado.prestador,
                    fecha_emision=now().date(),
                    impuestos=0,
                    monto_total=contrato.precio_acordado,
                    detalles=f"Servicio: {contrato.servicio_prestado.categoria.nombre} en {contrato.direccion}"
                )
                contrato.factura = factura

            contrato.save()
            return redirect('contratos_prestador')

    return render(request, 'contrato/actualizar_estado.html', {
        'contrato': contrato,
        'opciones_estado': Contrato.ESTADO_OPCIONES
    })
