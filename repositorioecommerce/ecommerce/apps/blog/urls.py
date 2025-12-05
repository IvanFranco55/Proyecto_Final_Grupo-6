from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('listar/', views.Listar_Productos, name = 'path_listar_productos'),

#detalle de un producto
    path('detalle/<int:pk>', views.Detalle_Producto_Clase.as_view(), name = 'path_detalle_producto'),
    
#ABM
    path('crear/', views.Crear_Producto.as_view(),name = 'path_crear_producto'),
    path('modificar/<int:pk>', views.Modificar_Producto.as_view(),name = 'path_modificar_producto'),
    path('Eliminar/<int:pk>', views.Eliminar_Producto.as_view(), name = 'path_eliminar_producto'),

#categoria
    path('blogxcategoria/<int:pk>', views.Filtro_categoria, name = 'path_filtro_categoria')
   
    path('listar/', views.Listar_articulos, name = 'path_listar_articulos'),

    path('detalle/<int:pk>', views.Detalle_Articulo_Clase.as_view(), name = 'path_detalle_articulo')

]
