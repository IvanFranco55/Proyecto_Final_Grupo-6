from django.shortcuts import render 

def Home(request):
    return render(request, 'general/home.html')

def Contacto(request):
    return render(request, 'general/contacto.html')

def Sobre_Nosotros(request):
    return render(request, 'general/sobre_nosotros.html')
