"""Define los formularios del modelo"""
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # (1)
        fields = ['text'] # (2)
        labels = {'text': ''} # (3)

    # Primero importamos el módulo forms y el modelo con el que vamos a trabajar (Topic). En el punto
    # (1) definimos una clase TopicForm, que hereda de ModelForm.
    # La versión más sencilla de un ModelForm consiste en una clase Meta anidada que dice a Django en que
    # módelo basar el formulario y que campos incluir en el mismo. En (2) creamos un formulario a partir del
    # modelo Topic e incluimos oslo el campo text. El siguiente campo (4)  le dice a Django que no genere una etiqueta
    # para le siguiente campo.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # (1)

# Actualizamos la sentencia import para que incluya Entry, además de Topic. Hacemos una nueva clase
# llamada  EntryForm que tiene una clase Meta anidada que recoge el modelo de base y el campo
# que hay que incluir en el formulario. De nuevo damos al campo 'text' una etiqueta en blanco.
# En (1) incluimos el atributo widgets. Un widget es un elemento del formulario HTML, como una caja
# con una sola línea de texto, un area de texto con varias lineas o una lista desplegable. Al incluir
# este atributo podemos anular la selección de widget predeterminada de Django. Si decimos a Django
# que use un elemento forms.Textearea estamos personalizando el widget de entrada para el campo 'text'
# de manera que el area de texto tenga una anchura de 80 columnas en vez de las 40 predeterminadas.