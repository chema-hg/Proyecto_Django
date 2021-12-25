""" Define patrones de URL para users."""

from django.urls import path, include

from . import views

app_name = 'users' # (1)

urlpatterns = [
    # incluye url de autentificación predeterminadas.
    path('', include('django.contrib.auth.urls')), # (2)
    # Página de registros de nuevos usuarios
    path('register/', views.register, name='register'), # (3)
]

# Importamos la función path y después la función include para poder incluir algunas
# URls de autentificación predeterminadas definidas por Django. Esta URLS predeterminadas incluyen
# patrones de URL con nombres como 'login' y 'loginout'. Configuramos la variable app_name como 'users' para
# que Django pueda distinguir estas urls de las que pertenecen a otras aplicaciones (1).

# El patrón de la página de inicio de sesión coincide con la URL http://localhost:8000/users/login/ (2)
# Cuando Django lee esta URL, la palabra clave users le dice que mire en users/urls.py y login que envie
# solicitudes a su vista login predeterminada.

# El patrón de la página para registrar nuevos usuarios utilizamos el UserCretionForm que ya tiene DAjngo
# preestablecido pero escribirimos nuestras propias funciones de vista y plantilla. (3) el patrón para
# esta página coincide con http://localhost:8000:/users/register/