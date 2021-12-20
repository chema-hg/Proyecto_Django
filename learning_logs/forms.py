"""Define los formularios del modelo"""
from django import forms

from .models import Topic

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
