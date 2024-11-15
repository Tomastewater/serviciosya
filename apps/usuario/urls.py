from .views import usuarioFormView, homeView
from django.urls import path
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('registrarse/', usuarioFormView.as_view(), name='add_user'),
    path('ingresar/', auth_view.LoginView.as_view(), name='login')
 
]
