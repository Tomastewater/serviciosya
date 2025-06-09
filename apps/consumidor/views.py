from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic
from django.urls import reverse_lazy
from apps.contrato.models import Contrato
from apps.ubicacion.models import Direccion
from apps.pago.models import Pago
from apps.ubicacion.form import DireccionForm, ModificarDireccionForm
from django.views.generic.edit import UpdateView, DeleteView

class ConsumidorPanelView(LoginRequiredMixin, generic.TemplateView):
    """
    Vista para mostrar el panel principal del consumidor.
    Requiere que el usuario esté autenticado.
    """
    template_name = 'consumidor_panel.html'

    def get_context_data(self, **kwargs):
        """
        Agrega el usuario actual al contexto de la plantilla.
        """
        usuario_actual = self.request.user
        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context

class ConsumidorDatosView(generic.TemplateView):
    """
    Vista para mostrar los datos personales del consumidor.
    """
    template_name = 'consumidor_datos_personales.html'

    def get_context_data(self, **kwargs):
        """
        Agrega el usuario actual al contexto de la plantilla.
        """
        usuario_actual = self.request.user
        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context

class ConsumidorDireccionListView(generic.ListView, generic.edit.FormMixin):
    """
    Vista para listar y agregar direcciones del consumidor.
    Permite mostrar las direcciones y agregar nuevas mediante un formulario.
    """
    model = Direccion
    template_name = "consumidor_direcciones.html"
    context_object_name = "direcciones"
    form_class = DireccionForm

    def get_queryset(self):
        """
        Filtra las direcciones por el usuario autenticado.
        """
        usuario_actual = self.request.user
        return Direccion.objects.filter(usuario=usuario_actual)

    def get_context_data(self, **kwargs):
        """
        Agrega el formulario al contexto de la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form() 
        return context
    
    def post(self, request, *args, **kwargs):
        """
        Maneja el envío del formulario para agregar una nueva dirección.
        """
        form = self.get_form()
        if form.is_valid():
            nueva_direccion = form.save(commit=False)
            nueva_direccion.usuario = self.request.user
            nueva_direccion.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Redirige a la misma página después de guardar la dirección.
        """
        return super().form_valid(form)

    def get_success_url(self):
        """
        Define la URL de redirección tras agregar una dirección.
        """
        return reverse_lazy('dire_consumidor')
    
class ModificarDireccionView(UpdateView):
    """
    Vista para modificar una dirección existente del consumidor.
    Solo permite modificar direcciones propias.
    """
    model = Direccion
    form_class = ModificarDireccionForm
    template_name = 'modificar_direccion.html'
    context_object_name = 'form'
    pk_url_kwarg = 'direccion_id'

    def get_object(self, queryset=None):
        """
        Obtiene la dirección a modificar y verifica que pertenezca al usuario autenticado.
        """
        direccion = super().get_object(queryset)
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para modificar esta dirección")
        return direccion

    def get_success_url(self):
        """
        Redirige a la lista de direcciones tras la modificación.
        """
        return reverse_lazy('dire_consumidor')
    
class EliminarDireccionView(DeleteView):
    """
    Vista para eliminar una dirección del consumidor.
    Solo permite eliminar direcciones propias.
    """
    model = Direccion
    template_name = 'eliminar_direccion.html'
    context_object_name = 'direccion'
    success_url = reverse_lazy('dire_consumidor')
    pk_url_kwarg = 'direccion_id'

    def get_object(self, queryset=None):
        """
        Obtiene la dirección a eliminar y verifica que pertenezca al usuario autenticado.
        """
        direccion = super().get_object(queryset)
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para eliminar esta dirección")
        return direccion

class ConsumidorPagosListView(generic.ListView):
    """
    Vista para listar los pagos realizados por el consumidor.
    """
    model = Pago
    template_name = "consumidor_pagos.html"
    context_object_name = "pagos"

    def get_queryset(self):
        """
        Filtra los pagos por el usuario autenticado.
        """
        usuario_actual = self.request.user
        pagos = Pago.objects.filter(contrato__consumidor__rol_usuario__usuario=usuario_actual)
        return pagos

class ConsumidorContratosListView(generic.ListView):
    """
    Vista para listar los contratos asociados al consumidor.
    """
    model = Contrato
    template_name = "consumidor_contratos.html"
    context_object_name = "contratos"

    def get_queryset(self):
        """
        Filtra los contratos por el usuario autenticado.
        """
        usuario_actual = self.request.user
        contratos = Contrato.objects.filter(consumidor__rol_usuario__usuario=usuario_actual)
        return contratos
