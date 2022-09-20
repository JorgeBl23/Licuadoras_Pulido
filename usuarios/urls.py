from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import Editarusuario, agregar_elemento, carrito, cusuario, detalle, eliminar_elemento, accesorio, limpiar_carrito, politicasprivacidad, producto, restar_elemento, serviciocliente, nosotros, tusuario, usuario_eliminar, vusuario

urlpatterns = [
    path('accesorios/', accesorio, name='usuarios-accesorios'),
    path('productos/', producto, name='usuarios-productos'),
    path('serviciocliente/', serviciocliente, name='usuarios-servicios'),
    path('nosotros/', nosotros, name='usuarios-nosotros'),
    path('carrito/', carrito, name='usuarios-carrito'),
    path('politicas/', politicasprivacidad, name='usuarios-politicas'),
    
    #usuarios
    path('crearusuario/', cusuario, name='usuario-crearUsuario'),
    path('tablausuario/', tusuario, name='usuario-tablaUsuario'),
    path('verusuario/<int:pk>', vusuario, name='usuario-verusuario'),
    path('editarusuario/<int:pk>', Editarusuario, name='usuario-editarusuario'),
    path('tablausuario/eliminar/<int:pk>/', usuario_eliminar, name='usuario-usuario-eliminar'),
    
    #carrito
    path('agregar/<int:elemento_id>/', agregar_elemento, name="agregar"),
    path('eliminar/<int:elemento_id>/', eliminar_elemento, name="eliminar"),
    path('restar/<int:elemento_id>/', restar_elemento, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    
    path('detalle/<int:pk>/<str:url_back>/', detalle, name="detalle")
]