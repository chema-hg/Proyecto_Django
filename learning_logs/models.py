from django.db import models

# Un módelo le dice a Django cómo trabajar con los datos que se guardarán en la aplicación.
# En lo que a código respecta un modelo es simplemente una clase: Tiene atributos y métodos.

# Create your models here.

class Topic(models.Model):
    """Un tema sobre el que está aprendiendo el usuario"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devuelve una representación del modelo como una cadena."""
        return self.text
# Hemos creado una clase llamada Topic que hereda de Model, una clase primaria incluida en Django que
# define la funcionalidad básica del modelo. Añadimos dos atributos: text y date_added.
# El atributo text es un Charfield, un dato formado por caracteres o texto. Usamos Charfield cuando queremos
# almacenar una pequeña cantidad de texto, como un nombre, un título o una ciudad. Cuando definimos un
# atributo Charfield tenemos que decir a Django cuanto espacio debería reservar en la base de datos.
# El atributo date_added es un DateTimeField, un dato que registrará la fecha y la hora. Le pasamos el
# argumento auto_now_add=True, para que establezca este atributo con la fecha y hora actuales cuando
# el usuario cree un tema nuevo.

# Para ver los distintos tipos de campos que puedemos usar en un modelo, vease:
# https://docs.djangoproject.com/en/4.0/ref/models/fields/

