from core.forms import SoftwareForm
from django.shortcuts import redirect, render
from .models import Software
from .forms import SoftwareForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def software(request):
    return render(request, 'software/software.html')

def videojuego(request):
    return render(request, 'juegos/videojuegos.html')

def formulario(request):
    software_form = SoftwareForm()
    return render(request, 'core/ingresar_software.html', {'software_form':software_form})

def form_software(request):
    if request.method == 'POST':
        software_form = SoftwareForm(request.POST)
        if software_form.is_valid():
            software_form.save()
            return redirect('index')
    else:
        software_form = SoftwareForm()
    
    return render(request, 'core/ingresar_software.html', {'software_form':software_form})

def verTodo(request):
    todo_software = Software.objects.all()

    return render(request, 'modificar/verTodo.html',
        context={'datos':todo_software}
    )

def mod_software(request, id):
    software = Software.objects.get(idSoftware = id)

    datos = {
        'form' : SoftwareForm(instance=software)
    }
    if request.method == 'POST':
        formulario = SoftwareForm(data=request.POST, instance=software)
        if formulario.is_valid:
            formulario.save()
            return redirect('verTodo')
    return render(request, 'modificar/modificar.html', datos)

def del_software(request, id):
    software = Software.objects.get(idSoftware = id)
    software.delete()
    return redirect('verTodo')
