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
    template_name = 'consumidor_panel.html'

    def get_context_data(self, **kwargs):

        usuario_actual = self.request.user

        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context


class ConsumidorDatosView(generic.TemplateView):
    template_name = 'consumidor_datos_personales.html'

    def get_context_data(self, **kwargs):

        usuario_actual = self.request.user

        context = super().get_context_data(**kwargs)
        context['usuario'] = usuario_actual
        return context

class ConsumidorDireccionListView(generic.ListView, generic.edit.FormMixin):
    model = Direccion
    template_name = "consumidor_direcciones.html"
    context_object_name = "direcciones"
    form_class = DireccionForm  # El formulario que usarás para agregar direcciones

    def get_queryset(self):
        # Filtra las direcciones según el usuario logueado
        usuario_actual = self.request.user
        return Direccion.objects.filter(usuario=usuario_actual)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form() 
        return context
    
    def post(self, request, *args, **kwargs):
        # Manejo del formulario al enviarse
        form = self.get_form()
        if form.is_valid():
            nueva_direccion = form.save(commit=False)
            nueva_direccion.usuario = self.request.user  # Asocia la dirección al usuario logueado
            nueva_direccion.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Redirige a la misma página después de guardar la dirección
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la misma página
        return reverse_lazy('dire_consumidor')
    
class ModificarDireccionView(UpdateView):
    model = Direccion
    form_class = ModificarDireccionForm
    template_name = 'modificar_direccion.html'
    context_object_name = 'form'

    # El campo que debe ser actualizado en la URL
    pk_url_kwarg = 'direccion_id'

    def get_object(self, queryset=None):
        # Obtén la dirección con el id proporcionado en la URL
        direccion = super().get_object(queryset)
        
        # Verifica que el usuario sea el propietario de la dirección
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para modificar esta dirección")
        
        return direccion

    def get_success_url(self):
        return reverse_lazy('dire_consumidor')
    
class EliminarDireccionView(DeleteView):
    model = Direccion
    template_name = 'eliminar_direccion.html'
    context_object_name = 'direccion'
    success_url = reverse_lazy('dire_consumidor')  # Redirige después de la eliminación

    pk_url_kwarg = 'direccion_id'  # Para usar el ID de la dirección en la URL

    def get_object(self, queryset=None):
        # Obtén la dirección con el id proporcionado en la URL
        direccion = super().get_object(queryset)
        
        # Verifica que el usuario sea el propietario de la dirección
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para eliminar esta dirección")
        
        return direccion

class ConsumidorPagosListView(generic.ListView):
    model = Pago
    template_name = "consumidor_pagos.html"
    context_object_name = "pagos"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        pagos = Pago.objects.filter(contrato__consumidor__rol_usuario__usuario=usuario_actual)

        return pagos

class ConsumidorContratosListView(generic.ListView):
    model = Contrato
    template_name = "consumidor_contratos.html"
    context_object_name = "contratos"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        contratos = Contrato.objects.filter(consumidor__rol_usuario__usuario=usuario_actual)

        return contratos
    