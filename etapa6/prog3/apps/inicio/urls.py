from django.urls import path

from .views import Home, LoginView, ErrorLogin, LogoutView


urlpatterns = [
    path('', Home, name='index'),
    path('usuarios/login', LoginView, name='login'),
    path('usuarios/error',ErrorLogin, name='errorlogin'),
    path('usuarios/logout', LogoutView, name='logout')
    
]