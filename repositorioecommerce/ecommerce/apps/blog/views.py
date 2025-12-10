from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Articulo, Categoria, Comentario
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo, FormularioModificarArticulo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def Listar_articulos(request):
    todos_articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()
    context = {}
    context['articulos'] = todos_articulos
    context['categorias'] = categorias
    
    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

def Filtro_Categoria(request, pk):
    ca = Categoria.objects.get(pk = pk)
    ar = Articulo.objects.filter(categoria = ca)
    categorias = Categoria.objects.all()
    context = {}
    context['articulos'] = ar
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)

def Buscador(request):
    if request.method == 'POST':
        busqueda = request.POST['busqueda']
        articulos = Articulo.objects.filter(titulo__icontains=busqueda)
        categorias = Categoria.objects.all()
        context = {}
        context['articulos'] = articulos
        context['categorias'] = categorias
        return render(request, 'blog/listar.html', context)
    
    return render(request, 'blog/listar.html')

def Filtro_Fecha(request, orden):
    if orden == 'antiguo':
        articulos = Articulo.objects.all().order_by('fecha_publicacion')
    else:
        articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    
    categorias = Categoria.objects.all()


    context = {}


    context['articulos'] = articulos
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)


class Crear_Articulo(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articulo
    template_name = 'blog/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class Modificar_Articulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    template_name = 'blog/modificar.html'
    form_class = FormularioModificarArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    def test_func(self):
        return self.request.user.is_staff

class Eliminar_Articulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
     model = Articulo
     template_name = 'blog/eliminar.html'
     success_url = reverse_lazy('blog:path_listar_articulos')

     def test_func(self):
        return self.request.user.is_staff

#LOGICA DE COMENTARIOS

@login_required 
def comentar(request, pk):
    articulo_seleccionado = Articulo.objects.get(pk=pk)
    usuario_actual = request.user
    
    texto_ingresado = request.POST.get('texto_comentado') 

    Comentario.objects.create(
        contenido = texto_ingresado, 
        autor = usuario_actual, 
        articulo = articulo_seleccionado
    )
    return HttpResponseRedirect(reverse_lazy('blog:path_detalle_articulo', kwargs={'pk': pk}))

@login_required 
def borrar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    id_articulo = comentario.articulo.pk

    if request.user == comentario.autor or request.user.is_staff:
        comentario.delete()

    return redirect('blog:path_detalle_articulo', pk=id_articulo)