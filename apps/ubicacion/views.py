from django.views.generic.edit import UpdateView, DeleteView
from .form import ModificarDireccionForm
from django.http import Http404
from .models import Direccion
from django.urls import reverse_lazy
    

class PrestadorModificarDireccionView(UpdateView):
    """
    Vista para modificar una dirección existente del prestador.

    Permite que el prestador edite únicamente sus propias direcciones.
    """
    model = Direccion
    form_class = ModificarDireccionForm
    template_name = 'modificar_direccion.html'
    context_object_name = 'form'
    pk_url_kwarg = 'direccion_id'

    def get_object(self, queryset=None):
        """
        Obtiene la dirección a modificar y verifica que pertenezca al usuario autenticado.

        Lanza Http404 si el usuario no es el propietario de la dirección.
        """
        direccion = super().get_object(queryset)
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para modificar esta dirección")
        return direccion

    def get_success_url(self):
        """
        Redirige a la lista de direcciones tras la modificación.
        """
        return reverse_lazy('direcciones')
    
class PrestadorEliminarDireccionView(DeleteView):
    """
    Vista para eliminar una dirección del prestador.

    Permite que el prestador elimine únicamente sus propias direcciones.
    """
    model = Direccion
    template_name = 'eliminar_direccion.html'
    context_object_name = 'direccion'
    success_url = reverse_lazy('direcciones')
    pk_url_kwarg = 'direccion_id'

    def get_object(self, queryset=None):
        """
        Obtiene la dirección a eliminar y verifica que pertenezca al usuario autenticado.

        Lanza Http404 si el usuario no es el propietario de la dirección.
        """
        direccion = super().get_object(queryset)
        if direccion.usuario != self.request.user:
            raise Http404("No tienes permiso para eliminar esta dirección")
        return direccion
    
    def get_success_url(self):
        """
        Redirige a la lista de direcciones tras la eliminación.
        """
        return reverse_lazy('direcciones')
