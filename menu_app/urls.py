from django.urls import path
from .views import menu, agregar_producto, eliminar_producto, menu_prueba, admin, inactivar_producto, activar_producto

urlpatterns = [
    path('', menu),
    path('menu_prueba/', menu_prueba),
    path('admin_menu/', admin, name = 'admin'),
    path('agregar_producto/', agregar_producto, name = 'agregar'),
    path('eliminar_producto/<id>', eliminar_producto),
    path('inactivar_producto/<id>', inactivar_producto),
    path('activar_producto/<id>', activar_producto),
]
