import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo_peliculas.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'rosita.garcia@tecsup.edu.pe', 'admin123')
    print("Superusuario creado exitosamente")
else:
    print("El usuario ya existe")
