from django.contrib import admin
from django.urls import path
from peliculas.views import lista_peliculas 
from django.conf import settings
from django.conf.urls.static import static
from peliculas.views import lista_peliculas, detalle_pelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_peliculas, name='index'),
    path('pelicula/<int:peli_id>/', detalle_pelicula, name='detalle'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
