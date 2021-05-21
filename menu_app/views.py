from io import DEFAULT_BUFFER_SIZE
from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Productos
import json

def view_prueba(request):
    elemento = request.POST.get()
    dato = {
        'proyecto_1': {'titulo': 'Proyectco #1',
                       'descripcion':'este es el proyecto #1',
                       'targets':'python, django'},
        'proyecto_2': {'titulo': 'Proyectco #2',
                       'descripcion':'este es el proyecto #2',
                       'targets':'python, django'},
        'proyecto_3': {'titulo': 'Proyectco #3',
                       'descripcion':'este es el proyecto #3',
                       'targets':'python, django'},
        'proyecto_4': {'titulo': 'Proyectco #4',
                       'descripcion':'este es el proyecto #4',
                       'targets':'python, django'},
    }
    json_data = json.dumps(dato)
    return render(request, 
                  "prueba.html", 
                  context={'time_series': json_data})


# Create your views here.
def menu(request):
    return render(request, 'menu.html', {})

def menu_prueba(request):
    productos = Productos.objects.all()
    return render(request, 'menu_prueba.html', {'productos':productos})

def agregar_producto(request):

    guardado = None

    try:
        titulo = request.POST['titulo'],
        descripcion = request.POST['descripcion'],
        precio = request.POST['precio']

        guardado =True

        new_product = Productos(
        titulo = titulo[0], 
        descripcion = descripcion[0], 
        precio = precio
        )

        if guardado == True:
            new_product.save()
    except:
        clave = None, 
        titulo = None, 
        descripcion = None, 
        precio = None, 
        guardado = None

    productos = Productos.objects.all()

    return render(request, 'admin.html', {'productos':productos})


def eliminar_producto(request, id):
    try:
        producto_eliminar = Productos.objects.get(id=id)
        producto_eliminar.delete()
        return redirect('agregar')
    except:
        return redirect('agregar')

    