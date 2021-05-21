from django.urls import path
from .views import menu, agregar_producto, eliminar_producto, menu_prueba

urlpatterns = [
    path('', menu),
    path('menu_prueba/', menu_prueba),
    path('agregar_producto/', agregar_producto, name = 'agregar'),
    path('eliminar_producto/<id>', eliminar_producto),
]
