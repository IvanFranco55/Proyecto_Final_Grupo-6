from django .shortcuts import render 
from .models import Articulo, Categoria
from django.views.generic import DetailView

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    return render(request, 'blog/listar.html', context)

