from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('listar/', views.Listar_articulos, name = 'path_listar_articulos')
    
]