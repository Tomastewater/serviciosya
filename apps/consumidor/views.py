from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from apps.contrato.models import Contrato
from apps.ubicacion.models import Direccion, Localidad, Provincia
from apps.consumidor.models import Consumidor
from apps.pago.models import Pago

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

class ConsumidorDireccionListView(generic.ListView):
    model = Direccion, Localidad, Provincia
    template_name = "consumidor_direcciones.html"
    context_object_name = "direcciones"

    def get_queryset(self):
        # Obtener el usuario logueado
        usuario_actual = self.request.user

        return Direccion.objects.filter(usuario = usuario_actual)

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
    