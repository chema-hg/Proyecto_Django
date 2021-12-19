"""Define los patrones URL para learning_logs
El hacer las páginas web requiere de 3 pasos:
- definir la url
- escribir vistas
- escribir plantillas."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
]
# urlpatterns es un lista de páginas individuales que se pueden solicitar a la aplicación learning logs.
# los argumentos de path() significan lo soguiente:
# el primero es una cadena que ayuda a enrutar la solicitud actual a una vista.
# el segundo es la función que se ejecutará en views.py al ejecutar la ruta anterior.
# el tercero aporta el nombre de 'index' para este patrón de url para que podamos referirnos a el en otras
# secciones del código. Siempre que queramos ofrecer un enlace para la página de inicio, usaremos este
# nombre en vez de escribir la url.