from django .shortcuts import render 
from .models import Articulo, Categoria
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # Para que solo entren logueados
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo, FormularioModificarArticulo

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    categorias = Categoria.objects.all()
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

class Crear_Articulo(CreateView):
    model = Articulo
    template_name = 'blog/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    def form_valid(self, form):
            form.instance.autor = self.request.user
            return super().form_valid(form)
            #esto es para que cuando querramos subir un articulo no pida el campo autor y asigne automaticamente al ususario

class Modificar_Articulo(UpdateView):
    model = Articulo
    template_name = 'blog/modificar.html'
    form_class = FormularioModificarArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

class Eliminar_Articulo(DeleteView):
     model = Articulo
     template_name = 'blog/eliminar.html'
     success_url = reverse_lazy('blog:path_listar_articulos')

def Filtro_Categoria(request, pk):
    ca = Categoria.objects.get(pk = pk)

    ar = Articulo.objects.filter(categoria = ca)
    context = {}
    context['articulos'] = ar
    categorias = Categoria.objects.all()
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)

# --- FUNCIÓN 1: BUSCADOR POR TÍTULO ---
def Buscador(request):
    # Primero chequeamos si mandaron algo (POST)
    if request.method == 'POST':
        # Agarramos lo que escribió el usuario en el input 'busqueda'
        busqueda = request.POST['busqueda']
        
        # Filtramos por título (icontains ignora mayúsculas/minúsculas)
        articulos = Articulo.objects.filter(titulo__icontains=busqueda)
        
        context = {
            'articulos': articulos,
            'categorias': Categoria.objects.all() # Para que no se rompa el menú lateral
        }
        return render(request, 'blog/listar.html', context)
    
    # Si entra por GET (sin buscar nada), lo mandamos al listar normal
    return render(request, 'blog/listar.html')


# --- FUNCIÓN 2: FILTRO POR FECHA ---
# --- FUNCIÓN: FILTRO POR FECHA (Ordena por antigüedad) ---
def Filtro_Fecha(request, orden):
    
    if orden == 'antiguo':
        # Orden ascendente (del más viejo al más nuevo)
        articulos = Articulo.objects.all().order_by('fecha_publicacion')
    else:
        # Por defecto: Orden descendente (del más nuevo al más viejo)
        articulos = Articulo.objects.all().order_by('-fecha_publicacion')

    context = {
        'articulos': articulos,
        'categorias': Categoria.objects.all() # Para mantener el menú lateral
    }
    
    return render(request, 'blog/listar.html', context)