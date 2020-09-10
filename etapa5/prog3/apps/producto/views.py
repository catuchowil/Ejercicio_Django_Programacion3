from django.shortcuts import render, redirect
from .models import Producto

from .forms import ProductoForm



# Create your views here.

"""
Esta es la vista inicial previo a traer los registros

def ListadoProducto(request):
    return render (request, 'producto/listado_producto.html')
"""

def ListadoProducto(request):

    prod = Producto.objects.all() # Trae todos los registros de la tabla
    return render(request, 'producto/listado_producto.html',{'producto':prod})



def IngresarProducto(request):

    if request.method == 'POST':
        produ_form = ProductoForm(request.POST)
        if produ_form.is_valid():
            produ_form.save()
            return redirect('producto:lista_producto')
    else:
        produ_form = ProductoForm()
    
    return render (request, 'producto/carga_producto.html',{'cargadatos':produ_form})



def EditarProducto(request, id):

    produ = Producto.objects.get(id=id)

    if request.method == 'GET':
        produ_form = ProductoForm(instance=produ)
    else:
        produ_form = ProductoForm(request.POST, instance=produ)
        if produ_form.is_valid():
            produ_form.save()
        return redirect('producto:lista_producto')
    
    return render(request, 'producto/carga_producto.html', {'cargadatos':produ_form, 'bande':1})


def EliminarProducto(request, id):

    produ = Producto.objects.get(id=id)

    if request.method == 'POST':
        produ.delete()
        return redirect('producto:lista_producto')
    
    return render(request, 'producto/eliminar_producto.html', {'datos':produ})



