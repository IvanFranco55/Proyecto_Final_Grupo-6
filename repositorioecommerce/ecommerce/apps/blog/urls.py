from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('listar/', views.Listar_articulos, name = 'path_listar_articulos'),

    path('detalle/<int:pk>', views.Detalle_Articulo_Clase.as_view(), name = 'path_detalle_articulo'),

    #CREAR
    path('crear/', views.Crear_Articulo.as_view(), name = 'path_crear_articulo'),

    #MODIFICAR

    path('modificar/<int:pk>', views.Modificar_Articulo.as_view(), name= 'path_modificar_articulo'),
    
    #ELIMINAR

    path('eliminar/<int:pk>', views.Eliminar_Articulo.as_view(), name= 'path_eliminar_articulo'),

    #FILTROS

    path('filtrarxcategoria/<int:pk>', views.Filtro_Categoria, name= 'path_filtrado_categoria'),

    path('buscador/', views.Buscador, name='path_buscador'),
    
    path('fecha/<str:orden>/', views.Filtro_Fecha, name='path_filtrado_fecha'),

    path ('comentar/<int:pk>', views.comentar, name= 'path_comentar'),

    path('borrar_comentario/<int:pk>/', views.borrar_comentario, name='path_borrar_comentario'),

    path('alfabetico/<str:orden>/', views.Filtro_Alfabetico, name='path_filtrado_alfabetico'),
]
    