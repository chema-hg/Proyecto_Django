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
    path('topics/', views.topics, name='topics'),
    # página de detalles sobre un tema individual.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Url de la nueva entrada new_topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Url de la nueva entrada new_entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Url para editar una entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
# urlpatterns es un lista de páginas individuales que se pueden solicitar a la aplicación learning logs.
# los argumentos de path() significan lo soguiente:
# el primero es una cadena que ayuda a enrutar la solicitud actual a una vista.
# el segundo es la función que se ejecutará en views.py al ejecutar la ruta anterior.
# el tercero aporta el nombre de 'index' para este patrón de url para que podamos referirnos a el en otras
# secciones del código. Siempre que queramos ofrecer un enlace para la página de inicio, usaremos este
# nombre en vez de escribir la url.