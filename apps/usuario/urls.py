from .views import usuarioFormView, homeView, aboutView, registerView
from django.urls import path


urlpatterns = [

    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='register'),
    path('acercade/', aboutView.as_view(), name='about'),
    # path('registrarse/', registerView.as_view(), name='register'),
    
]
