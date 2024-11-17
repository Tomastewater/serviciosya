from django.views import generic
from .form import usuarioForm
from django.urls import reverse_lazy
from django.shortcuts import render

class usuarioFormView(generic.FormView):
    template_name = 'formRegistrarse.html'
    form_class = usuarioForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class registerView(generic.TemplateView):
    template_name = 'register.html'

class homeView(generic.TemplateView):
    template_name = 'home.html'

class aboutView(generic.TemplateView):
    template_name = 'about.html'