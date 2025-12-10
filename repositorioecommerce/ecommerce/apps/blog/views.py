from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Articulo, Categoria, Comentario
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo, FormularioModificarArticulo
from django.contrib.auth.decorators import login_required

# --- IMPORTAMOS LA SEGURIDAD ---
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# ==============================================================================
#                               VISTAS PUBLICAS
# ==============================================================================

def Listar_articulos(request):
    todos_articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()
    context = {'articulos': todos_articulos, 'categorias': categorias}
    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

def Filtro_Categoria(request, pk):
    ca = Categoria.objects.get(pk = pk)
    ar = Articulo.objects.filter(categoria = ca)
    context = {'articulos': ar, 'categorias': Categoria.objects.all()}
    return render(request, 'blog/listar.html', context)

def Buscador(request):
    if request.method == 'POST':
        busqueda = request.POST['busqueda']
        articulos = Articulo.objects.filter(titulo__icontains=busqueda)
        context = {'articulos': articulos, 'categorias': Categoria.objects.all()}
        return render(request, 'blog/listar.html', context)
    return render(request, 'blog/listar.html')

def Filtro_Fecha(request, orden):
    if orden == 'antiguo':
        articulos = Articulo.objects.all().order_by('fecha_publicacion')
    else:
        articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    context = {'articulos': articulos, 'categorias': Categoria.objects.all()}
    return render(request, 'blog/listar.html', context)


# ==============================================================================
#                     VISTAS RESTRINGIDAS (SOLO STAFF)
# ==============================================================================

# CREAR: Solo Staff
class Crear_Articulo(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = 'blog/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    # 1. Asigna el autor automáticamente
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    # 2. REGLA DE SEGURIDAD: ¿Es Staff?
    def test_func(self):
        return self.request.user.is_staff

# MODIFICAR: Solo Staff
class Modificar_Articulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    template_name = 'blog/modificar.html'
    form_class = FormularioModificarArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    def test_func(self):
        return self.request.user.is_staff

# ELIMINAR: Solo Staff
class Eliminar_Articulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
     model = Articulo
     template_name = 'blog/eliminar.html'
     success_url = reverse_lazy('blog:path_listar_articulos')

     def test_func(self):
        return self.request.user.is_staff


# ==============================================================================
#                       LOGICA DE COMENTARIOS
# ==============================================================================

@login_required # <--- OBLIGATORIO ESTAR LOGUEADO PARA COMENTAR
def comentar(request, pk):
    articulo_seleccionado = Articulo.objects.get(pk=pk)
    usuario_actual = request.user
    
    # Busca 'texto_comentado' porque así lo pusiste en el HTML
    texto_ingresado = request.POST.get('texto_comentado') 

    Comentario.objects.create(
        contenido = texto_ingresado, 
        autor = usuario_actual, 
        articulo = articulo_seleccionado
    )
    return HttpResponseRedirect(reverse_lazy('blog:path_detalle_articulo', kwargs={'pk': pk}))

@login_required # <--- OBLIGATORIO PARA BORRAR
def borrar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    id_articulo = comentario.articulo.pk

    # LOGICA: ¿Es el dueño O es Staff?
    if request.user == comentario.autor or request.user.is_staff:
        comentario.delete()

    return redirect('blog:path_detalle_articulo', pk=id_articulo)