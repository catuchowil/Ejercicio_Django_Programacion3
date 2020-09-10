from django.shortcuts import render

# Create your views here.
def ListadoProducto(request):
    return render (request, 'producto/listado_producto.html')
