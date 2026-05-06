from django.shortcuts import get_object_or_404, render
from .models import Pelicula
from .models import Genero
from django.db import models

def lista_peliculas(request):
    # Obtenemos los parámetros de la URL
    q = request.GET.get('q', '')
    genero_id = request.GET.get('genero', '')

    # Empezamos con todas las películas
    peliculas = Pelicula.objects.all()

    # Filtro por nombre o director (Busca en ambos campos a la vez)
    if q:
        peliculas = peliculas.filter(
            models.Q(titulo__icontains=q) | 
            models.Q(director__nombre__icontains=q)
        )

    # Filtro por categoría (Género)
    if genero_id:
        peliculas = peliculas.filter(genero_id=genero_id)

    # Necesitamos enviar todos los géneros para armar el menú de categorías
    generos = Genero.objects.all()

    return render(request, 'peliculas/index.html', {
        'peliculas': peliculas,
        'generos': generos
    })

def detalle_pelicula(request, peli_id):
    pelicula = get_object_or_404(Pelicula, id=peli_id)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})
