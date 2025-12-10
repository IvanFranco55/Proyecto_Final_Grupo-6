from django import forms
from .models import Articulo

class FormularioCrearArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen', 'categoria']
        
        # ESTO ES MAGIA: Le decimos a Django "Ponele la clase CSS 'input-hacker' a todo"
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input-hacker', 'placeholder': 'Título del Informe...'}),
            'contenido': forms.Textarea(attrs={'class': 'input-hacker', 'rows': 5, 'placeholder': 'Desarrollo del contenido...'}),
            'categoria': forms.Select(attrs={'class': 'input-hacker'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'input-hacker'}),
        }

class FormularioModificarArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen', 'categoria']
        
        # Lo mismo para modificar, mantenemos el estilo
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input-hacker'}),
            'contenido': forms.Textarea(attrs={'class': 'input-hacker', 'rows': 5}),
            'categoria': forms.Select(attrs={'class': 'input-hacker'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'input-hacker'}),
        }