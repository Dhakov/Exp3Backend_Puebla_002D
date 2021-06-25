from core.forms import SoftwareForm
from django.shortcuts import redirect, render
from .models import Software
from .forms import SoftwareForm

# Create your views here.

def index(request):

    aplicaciones = Software.objects.all()

    return render(request, 'index.html', 
        context={'datos':aplicaciones}
    )

def software(request):
    return render(request, 'software.html')


def form_software(request):
    if request.method == 'POST':
        software_form = SoftwareForm(request.POST)
        if software_form.is_valid():
            software_form.save()
            return redirect('index')
    else:
        software_form = SoftwareForm()
    return render(request, 'core/ingresar_software.html', {'software_form':software_form})

