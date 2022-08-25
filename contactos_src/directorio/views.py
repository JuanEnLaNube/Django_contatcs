from django.shortcuts import render, redirect
from directorio.models import Contactos
from django.contrib import messages
from directorio.forms import ContactosForm

# Create your views here.
def inicio_view(request):

    if request.method == 'GET':
        context = {}

        if Contactos.objects.count() == 0:    
            messages.info(request,'Bienvenido, puedes registrar tu primer contacto ahora.')    
        
        else:
            mis_contactos = Contactos.objects.all()
            context = { 'mis_contactos':mis_contactos}
        return render(request, 'directorio/index.html', context)
    elif request.method == 'POST':

        form = ContactosForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(request)
            messages.success(request,'¡Éxito! Se registró el contacto correctamente.')
        else:
            messages.error(request,'Error! Por favor revisa la información e intenta nuevamente.')
        
        return redirect('Inicio')
        

   