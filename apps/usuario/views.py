from django.views import generic
from .form import usuarioForm
from django.urls import reverse_lazy
from django.shortcuts import render

class usuarioFormView(generic.FormView):
    template_name = 'agregarUsuario.html'
    form_class = usuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class homeView(generic.TemplateView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')