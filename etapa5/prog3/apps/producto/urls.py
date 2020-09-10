from django.urls import path

from .views import ListadoProducto, IngresarProducto, EditarProducto, EliminarProducto

urlpatterns = [
    
    path('listado/',ListadoProducto, name='lista_producto'),
    path('ingresar/',IngresarProducto, name='ingreso_producto'),
    path('editar/<int:id>',EditarProducto, name='editar_producto'),
    path('eliminar/<int:id>', EliminarProducto, name = 'eliminar_producto')

]