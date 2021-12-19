from django.shortcuts import render

# Create your views here.

# Una función de vista coge la información de una solicitud , prepara los datos necesarios para generar la
# página y los envia de vuelta al navegador, con frecuencia usando una plantilla que define el aspecto
# de la página.

def index(request):
    """La página de inicio de learning_logs"""
    return render(request, 'learning_logs/index.html')
