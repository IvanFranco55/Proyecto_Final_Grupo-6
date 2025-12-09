from django.shortcuts import render 
from django.apps import apps 

def Home(request):

    Articulo = apps.get_model('blog', 'Articulo')

    ultimos_articulos = Articulo.objects.all().order_by('-fecha_publicacion')[:6]
    context = {}
    context['articulos'] = ultimos_articulos
    
    return render(request, 'general/home.html', context)

def Contacto(request):
    return render(request, 'general/contacto.html')

def Sobre_Nosotros(request):
    return render(request, 'general/sobre_nosotros.html')

