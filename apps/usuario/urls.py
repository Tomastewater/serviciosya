from .views import usuarioFormView, homeView, aboutView
from django.urls import path


urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('about/', aboutView.as_view(), name='about'),

    
]
