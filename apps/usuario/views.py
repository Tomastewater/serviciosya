from django.views import generic
from .form import usuarioForm
from django.urls import reverse_lazy

class usuarioFormView(generic.FormView):
    template_name = 'agregarUsuario.html'
    form_class = usuarioForm
    success_url = reverse_lazy('add_user')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


