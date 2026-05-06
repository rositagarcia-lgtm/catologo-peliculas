from django.db import models

#Tabla género
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


# Tabla para los Directores
class Director(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Tabla para las Películas
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField() # Usamos 'anio' porque la 'ñ' puede dar problemas en código
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    
    # RELACIONES 
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo