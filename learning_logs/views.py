from django.shortcuts import render

from .models import Topic  # (1)


# Create your views here.

# Una función de vista coge la información de una solicitud , prepara los datos necesarios para generar la
# página y los envia de vuelta al navegador, con frecuencia usando una plantilla que define el aspecto
# de la página.

def index(request):
    """La página de inicio de learning_logs"""
    return render(request, 'learning_logs/index.html')


def topics(request):  # (2)
    "Muestra todos los temas."
    topics = Topic.objects.order_by('date_added')  # (3)
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)  # (4)


# Primero importamos el modelo asociado con los datos que necesitamos (1). la función
# topics() necesita un parámetro, que es el objeto request que Django recibe del servidor. (2)
# En (3) consultamos la base de datos pidiendo los objetos Topic, ordenados por el atributo
# date_added. La consulta resultante se almacena en topics.
# En (4) definimos un contexto que enviaremos a la plantilla. Un contexto es un diccionario en el que las claves
# son nombres que usaremos en la plantilla para acceder a los datos y los valores son los datos que tenemos
# que enviar a la plantilla.

def topic(request, topic_id):  # (1)
    """Muestra un tema concreto y todas sus entradas."""
    topic = Topic.objects.get(id=topic_id)  # (2)
    entries = topic.entry_set.order_by('-date_added')  # (3)
    context = {'topic': topic, 'entries': entries}  # (4)
    return render(request, 'learning_logs/topic.html', context)  # (5)
# Esta es la primera función de vista que requiere un párametro distinto del objeto request. La función
# acepta el valor capturado por la expresión /<int:topic_id>/ y lo guarda en topic_id (1). En (2)
# usamos get() para recuperar el tema, igual que hicimos en el intérprete de Django. En (3) obtenemos las
# entradas asociadas a ese tema y las ordenamos segun date_added. El signo negativo delante de date_added
# ordena los resultados en orden inverso, mostrando primero las entradas más recientes. Guardamos el tema
# y las entradas en el diccionario context (4) y lo enviamos a la plantilla topic.html (5)

# NOTA: las frases de código (2) y (3) se llaman consultas porque consultan la base de datos en busca
# de información especifica. Cuando escribamos consultas es conveniente probarlas en el shell de Django
# para tener una idea clara de lo que devuelven.

# IMPORTANTE: Hay una diferencia sutil pero importante, entre topic.id y topic_id. La expresión
# topic.id examina un tema y recupera el valor de la ID correspondiente. La variable topic_id es una
# referncia a ese ID en el código.

# La documentación sobre plantillas de django se encuentra en:
# https://docs.djangoproject.com/es/4.0/ref/templates/
