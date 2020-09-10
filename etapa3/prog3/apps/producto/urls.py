from django.urls import path

from .views import ListadoProducto

urlpatterns = [
    path('listado/',ListadoProducto, name='lista_producto')
]