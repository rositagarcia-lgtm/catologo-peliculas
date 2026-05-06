from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('panel-admin/', views.panel_admin, name='panel_admin'),
    path('pelicula/<int:peli_id>/', views.detalle_pelicula, name='detalle_pelicula'),

    path('peliculas/crear/', views.crear_pelicula, name='crear_pelicula'),
    path('peliculas/editar/<int:peli_id>/', views.editar_pelicula, name='editar_pelicula'),
    path('peliculas/eliminar/<int:peli_id>/', views.eliminar_pelicula, name='eliminar_pelicula'),

    path('generos/', views.lista_generos, name='lista_generos'),
    path('generos/crear/', views.crear_genero, name='crear_genero'),
    path('generos/editar/<int:genero_id>/', views.editar_genero, name='editar_genero'),
    path('generos/eliminar/<int:genero_id>/', views.eliminar_genero, name='eliminar_genero'),

    path('directores/', views.lista_directores, name='lista_directores'),
    path('directores/crear/', views.crear_director, name='crear_director'),
    path('directores/editar/<int:director_id>/', views.editar_director, name='editar_director'),
    path('directores/eliminar/<int:director_id>/', views.eliminar_director, name='eliminar_director'),
]