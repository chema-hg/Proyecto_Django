from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """ Vista para registrar nuevos usuarios."""
    if request.method != 'POST':
        # Muestra un formulario de registro en blanco al entrar por primera vez.
        form = UserCreationForm() # (1)
    else:
        # Procesa un formulario ya cumplimentado
        form = UserCreationForm(data=request.POST) # (2)

        if form.is_valid(): # (3)
            new_user = form.save() # (4)
            # Inicia la sesión del usuario y lo redirige a la página de inicio.
            login(request, new_user) # (5)
            return redirect('learning_logs:index') # (6)

    # Muestra un formulario en blanco o no válido.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

    # La función de vista register() necesita mostrar un formulario de registro en blanco cuando
    # se solicite la página de registro por primera vez y luego procesar los formularios cumplimentados
    # cuando se envíen. Cuando se realiza un registro, la función también necesita iniciar la sesión
    # del usuario de nuevo.

    # Importamos las funciones render() y redirect() y también la función login() para iniciar la
    # sesión del usuario si su información de registro es correcta. También importamos el UserCreationForm
    # predeterminado. En la función register() comprobamos si estamos respondiendo a una solicitud POST.
    # Si no es el caso, hacemos una instancia de UserCreationForm sin datos iniciales. (1)

    # Si estamos respondiendo a una solicitud POST, hacemos una instancia de UserCreationForm basada en los
    # datos enviados (2). Comprobamos que los datos son válidos (3), en este caso, que el nombre del usuario
    # tiene los caracteres apropiados, que las contraseñas coinciden y que el usuario no está intentando
    # hacer un envío malicioso.

    # Si los datos enviados son válidos, llamamos al método save() del formulario para guardar el nombre de usuario
    # y el hash de la contraseña en la base de datos (4) Este método devuelve el objeto de usuario recién
    # creado, que asignamos a new_user. Cuando se guarda la información del usuario, iniciamos su sesión
    # llamando a la función login() con los objetos request y new_user (5). lo cual crea una sesión válida
    # para el nuevo usuario. Por último, redirigimos al usuario a la página de inicio (6), donde un saludo
    # personalizado en el encabezado le indica que el registro es correcto. Al final de la función, representamos,
    # la página, que será un formulario en blanco o un formulario enviado que no es válido.


