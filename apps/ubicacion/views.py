from django.views.generic.edit import UpdateView, DeleteView
from .form import ModificarDireccionForm
from django.http import Http404
from .models import Direccion
from django.urls import reverse_lazy

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
    

class PrestadorModificarDireccionView(UpdateView):
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
        return reverse_lazy('direcciones')
    
class PrestadorEliminarDireccionView(DeleteView):
    model = Direccion
    template_name = 'eliminar_direccion.html'
    context_object_name = 'direccion'
    success_url = reverse_lazy('direcciones')  # Redirige después de la eliminación

    pk_url_kwarg = 'direccion_id'  # Para usar el ID de la dirección en la URL

    def get_object(self, queryset=None):
        # Obtén la dirección con el id proporcionado en la URL
        direccion = super().get_object(queryset)
        
        # Verifica que el usuario sea el propietario de la dirección
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para eliminar esta dirección")
        
        return direccion
    
    def get_success_url(self):
        return reverse_lazy('direcciones')     
