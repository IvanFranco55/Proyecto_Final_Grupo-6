from django.shortcuts import render
from .models import Articulo, Categoria
from django.views.generic import DetailView


#Categoria
def Filtro_categoria(request,pk):
    ctg = Categoria.objects.get(pk= pk)
    art= Articulo.objects.filter(Categoria= ctg)
    context = {}
    context['blog'] = art
    return render(request,'blog/categoria.html', context)
  

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

