from django.urls import path
from administrador.models import Favorito
from administrador.views import copiaseguridad, electrodomestico_favorito, electrodomestico, electrodomestico_editar, electrodomestico_eliminar, elemento, elemento_editar, elemento_eliminar, inicioadmin, marca, marca_editar, marca_eliminar, servicio, servicio_editar, servicio_eliminar, tipoelemento, tipoelemento_editar, tipoelemento_eliminar,stock

urlpatterns = [
    path('inicioadmin/', inicioadmin, name='administrador-inicioadmin'),

    path('categoria/', tipoelemento, name='administrador-categoria'),
    path('categoria/u/<int:pk>/', tipoelemento_editar, name='administrador-categoria-editar'),
    path('categoria/d/<int:pk>/', tipoelemento_eliminar, name='administrador-categoria-eliminar'),
    
    path('elemento/', elemento, name='administrador-elemento'),
    path('elemento/u/<int:pk>/', elemento_editar, name='administrador-elemento-editar'),
    path('elemento/d/<int:pk>/', elemento_eliminar, name='administrador-elemento-eliminar'),
    
    path('marca/', marca, name='administrador-marca'),
    path('marca/u/<int:pk>/', marca_editar, name='administrador-marca-editar'),
    path('marca/d/<int:pk>/', marca_eliminar, name='administrador-marca-eliminar'),
    
    path('electrodomestico/', electrodomestico, name='administrador-electrodomestico'),
    path('electrodomestico/u/<int:pk>/', electrodomestico_editar, name='administrador-electrodomestico-editar'),
    path('electrodomestico/d/<int:pk>/', electrodomestico_eliminar, name='administrador-electrodomestico-eliminar'),
    path('electrodomestico/f/<int:pk>/', electrodomestico_favorito, name='administrador-electrodomestico-favorito'),
    
    path('servicio/', servicio, name='administrador-servicio'),
    path('servicio/u/<int:pk>/', servicio_editar, name='administrador-servicio-editar'),
    path('servicio/d/<int:pk>/', servicio_eliminar, name='administrador-servicio-eliminar'),
    
    path('copiaseguridad/<str:tipo>/', copiaseguridad, name='administrador-copiaseguridad'),
    path('stock/l/<int:pk>', stock ,name='elemento-stock')
]