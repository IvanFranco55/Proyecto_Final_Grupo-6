from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home, name = 'path_home'),
    path('contacto/', views.Contacto, name = 'path_contacto'),
    path('sobre_nosotros/', views.Sobre_Nosotros, name = 'path_sobre_nosotros')
    path('blog/', include('blog.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
