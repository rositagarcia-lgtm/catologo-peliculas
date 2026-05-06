from django.shortcuts import get_object_or_404, render, redirect
from django.db import models

from .models import Pelicula, Genero, Director
from .forms import PeliculaForm, GeneroForm, DirectorForm


def lista_peliculas(request):
    q = request.GET.get('q', '')
    genero_id = request.GET.get('genero', '')

    peliculas = Pelicula.objects.all()

    if q:
        peliculas = peliculas.filter(
            models.Q(titulo__icontains=q) |
            models.Q(director__nombre__icontains=q)
        )

    if genero_id:
        peliculas = peliculas.filter(genero_id=genero_id)

    generos = Genero.objects.all()

    return render(request, 'peliculas/index.html', {
        'peliculas': peliculas,
        'generos': generos
    })


def detalle_pelicula(request, peli_id):
    pelicula = get_object_or_404(Pelicula, id=peli_id)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})


# CRUD PELICULA

def crear_pelicula(request):
    form = PeliculaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_pelicula.html', {'form': form})


def editar_pelicula(request, peli_id):
    pelicula = get_object_or_404(Pelicula, id=peli_id)

    form = PeliculaForm(
        request.POST or None,
        request.FILES or None,
        instance=pelicula
    )

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_pelicula.html', {'form': form})


def eliminar_pelicula(request, peli_id):
    pelicula = get_object_or_404(Pelicula, id=peli_id)

    if request.method == 'POST':
        pelicula.delete()
        return redirect('panel_admin')

    return render(request, 'peliculas/eliminar_pelicula.html', {
        'pelicula': pelicula
    })


# CRUD GENERO

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'peliculas/lista_generos.html', {'generos': generos})


def crear_genero(request):
    form = GeneroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_genero.html', {'form': form})


def editar_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    form = GeneroForm(request.POST or None, instance=genero)

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_genero.html', {'form': form})


def eliminar_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)

    if request.method == 'POST':
        genero.delete()
        return redirect('panel_admin')

    return render(request, 'peliculas/eliminar_genero.html', {'genero': genero})


# CRUD DIRECTOR

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'peliculas/lista_directores.html', {'directores': directores})


def crear_director(request):
    form = DirectorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_director.html', {'form': form})


def editar_director(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    form = DirectorForm(request.POST or None, instance=director)

    if form.is_valid():
        form.save()
        return redirect('panel_admin')

    return render(request, 'peliculas/form_director.html', {'form': form})


def eliminar_director(request, director_id):
    director = get_object_or_404(Director, id=director_id)

    if request.method == 'POST':
        director.delete()
        return redirect('panel_admin')
    return render(request, 'peliculas/eliminar_director.html', {
        'director': director
    })

def panel_admin(request):
    peliculas = Pelicula.objects.all()
    generos = Genero.objects.all()
    directores = Director.objects.all()

    return render(request, 'peliculas/panel_admin.html', {
        'peliculas': peliculas,
        'generos': generos,
        'directores': directores
    })