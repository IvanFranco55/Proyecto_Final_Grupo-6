from django.shortcuts import render
from .models import Articulo, Categoria

# Create your views here.

#Categoria
def Filtro_categoria(request,pk):
    ctg = Categoria.objects.get(pk= pk)
    art= Articulo.objects.filter(Categoria= ctg)
    context = {}
    context['blog'] = art
    return render(request,'blog/categoria.html', context)