from django.urls import path

from .views import ListadoProducto, IngresarProducto

urlpatterns = [
    
    path('listado/',ListadoProducto, name='lista_producto'),
    path('ingresar/',IngresarProducto, name='ingreso_producto')
]