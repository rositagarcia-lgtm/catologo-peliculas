from django import forms
from .models import Genero, Director, Pelicula


# FORMULARIO GÉNERO
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del género'
            }),
        }


# FORMULARIO DIRECTOR
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre', 'pais']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del director'
            }),

            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el país'
            }),
        }


# FORMULARIO PELÍCULA
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'anio', 'poster', 'genero', 'director']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título'
            }),

            'anio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el año'
            }),

            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),

            'director': forms.Select(attrs={
                'class': 'form-select'
            }),
        }