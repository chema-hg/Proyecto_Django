from django.shortcuts import render, redirect

from .models import Topic  # (1)
from .forms import TopicForm, EntryForm


# Create your views here.

# Una función de vista coge la información de una solicitud , prepara los datos necesarios para generar la
# página y los envía de vuelta al navegador, con frecuencia usando una plantilla que define el aspecto
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

def new_topic(request):
    """Añade un tema nuevo"""
    if request.method != 'POST':  # (1)
        # no se han enviado los datos; creamos un formulario en blanco.
        form = TopicForm()  # (2)
    else:
        # Datos enviados mediante POST, hay que procesarlo.
        form = TopicForm(data=request.POST)  # (3)
        if form.is_valid():  # (4)
            form.save()  # (5)
            return redirect('learning_logs:topics')  # (6)
    # Muestra un formulario en blanco o no valido.
    context = {'form': form}  # (7)
    return render(request, 'learning_logs/new_topic.html', context)


# La función new_topic() necesita manejar dos tipos de situaciones diferentes:
# - Solicitudes iniciales de la página new_topic (en donde hay que mostrar el formulario en blanco,
# y el procesamiento de la información enviada con el formulario. Y una vez procesada la información
# hay que mandarle de vuelta al sitio topics.
# Empezamos importando la función redirect, que usaremos para redirigir al usuario a la página topics
# después de enviar su tema. La función redirect() coge el nombre de una vista y redirige alli al usuario.
# También importamos el formulario que acabamos de escribir. TopicForm.

# El condicional en (1) establece si la solicitud es GET o POST. Si no es post es probable que la
# solicitud sea GET y por tanto tengamos que mostrar el formulario en blanco. Creamos una instancia de
# TopicForm en (2) y se la asignamos a la variable form y enviamos el formulario a la plantilla en el
# diccionario context. Como no incluimos argumentos al crear la instancia de TopicForm, Django crea un
# formulario en blanco que el usuario pueda rellenar.
# Si la solicitud es POST se ejecuta el bloque else y procesa los datos introducidos por el usuario,
# y guardamos en request.POST. El objeto form devuelto contiene la información enviada por el usuario (3).
# Sin embargo no podemos guardar la información en la base de datos sin antes comprobamos que es válida.
# (4) el método is_valid() comprueba que se han rellenado todos los campos obligatorios, (que por defecto
# todos lo son) y que coinciden con los tipos de campos esperados, por ejemplo que la longitud de text
# es menor que 200 caracteres, como especificamos en models.py. Esta validación automática ahorra mucho
# trabajo. Si es correcto llamamos a save() (5) que escribe los datos del formulario en la base de
# datos. Una vez guardados los datos llamamos a redirect para redirigir al navegador a la página topics.

# La variable context se define al final de la función de vista y la página se muestra con la plantilla
# new_topic.html. Este código se coloca fuera de cualquier bloque if; se ejecutara si se ha creado un
# formulario en blanco y también si se ha enviado un formulario que no se considera válido. Un formulario
# no válido incluirá mensajes de error predeterminados para ayudar al usuario a enviar datos aceptables.

def new_entry(request, topic_id):
    """Añade una entrada nueva para un tema particular."""
    topic = Topic.objects.get(id=topic_id)  # (1)

    if request.method != 'POST':  # (2)
        # No se han enviado datos y por tanto se crea un formulario en blanco.
        form = EntryForm()  # (3)
    else:
        # Datos POST enviados; procesa los datos.
        form = EntryForm(data=request.POST)  # (4)
        if form.is_valid():
            new_entry = form.save(commit=False)  # (5)
            new_entry.topic = topic # (6)
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)  # (7)

    # Muestra un formulario en blanco o no válido.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

    # Actualizamos la sentencia import par que incluya el EntryForm. La definición de new_entry() tiene
# que ser un paŕametro topic_id para almacenar el valor que recibe de la URL. Necesitaremos el tema para
# renderizar la página y procesar los datos del formulario, asi que usamos topic_id para obtener el objeto
# de tema correcto en (1)

# En (2) comprobamos si el método de solicitud es POST o GET. El bloque if se ejecuta si se trata de una
# solicitud GET y se crea una instancia en blanco de EntryForm (3). Si el método de la solicitud es POST,
# procesamos los datos haciendo una instancia de EntryForm. con los datos POST del objeto request (4)
# Después comprobamos si el formulario es válido. Si lo es necesitamos configurar el atributo topic
# antes de guardarlo en la base de datos. Cuando llamemos a save() incluimos el argumento commit=False (5)
# para que se cree un nuevo objeto de entrada y lo asigne a new_entry sin guardarlo todavía en la base
# de datos. Configuramos el atributo topic de new_entry con el tema extraido de la base de datos al
# principio de la función (6). DEspues llamamos a save() sin argumentos, guardando la entrada en la
# base de datos con el tema correcto ya asociado.

# La llamada a redirect() en (7) requiere de dos argumentos: el nombre de la vista donde queremos redi-
# rigir y el argumento que necesita esa función de vista. Aquí estamos redirigiendo a topic() que requiere
# el argumento topic_id. Esa vista muestra la página del tema para la que el usuario ha hecho la entrada
# y debería verse la entrada para la lista de entradas.
