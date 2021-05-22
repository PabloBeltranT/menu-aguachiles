from io import DEFAULT_BUFFER_SIZE
from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Productos
from .forms import Img
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

def admin(request):
    productos = Productos.objects.all()
    return render(request, 'admin.html', {'productos':productos, 'form_img':Img})

def agregar_producto(request):
    

    try:
        titulo = str(request.POST['titulo'])
    except:
        return redirect('admin')
    try:
        descripcion = str(request.POST['descripcion'])
    except:
        return redirect('admin')
    try:
        precio = int(request.POST['precio'])
    except:
        return redirect('admin')
    try:
        estado = bool(request.POST['estado'])
    except:
        estado = False


    try:
        producto_repetido = Productos.objects.get(titulo = titulo)
    except:
        producto_repetido = False

    if producto_repetido == False:
        new_product = Productos(
        titulo = titulo,
        descripcion = descripcion,
        precio = precio,
        estado = estado
        )
        new_product.save()

    return redirect('admin')


def eliminar_producto(request, id):
    try:
        producto_eliminar = Productos.objects.get(id=id)
        producto_eliminar.delete()
        return redirect('admin')
    except:
        return redirect('admin')

def inactivar_producto(request, id):
    try:
        producto_inactivar = Productos.objects.get(id=id)
        producto_inactivar.estado = False
        producto_inactivar.save()
        return redirect('admin')
    except:
        return redirect('admin')

def activar_producto(request, id):
    try:
        producto_activar = Productos.objects.get(id=id)
        producto_activar.estado = True
        producto_activar.save()
        return redirect('admin')
    except:
        return redirect('admin')

    