from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .serializers import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
import requests

#metodos para listar desde el api
def periodistasapi(request):
    response = requests.get('http://127.0.0.1:8000/api/periodistas/')
    
    periodistas = response.json()
    

    aux = {
        'listas' : periodistas,
    }

    return render(request, 'core/periodista/crudapi/index.html', aux)

def index(request):
    response = requests.get('http://alpha-meme-maker.herokuapp.com/:page')
    horoscopo = response.json()

    aux = {
        'horoscopo' : horoscopo
    }
    return render(request,'core/index.html',aux)

#UTILIZAMOS LAS VIEWSET PARA MANEJAR LAS PETICIONES HTTP(GET,POST,PUT,DELETE)
class TipoPeriodistaViewset(viewsets.ModelViewSet):
    queryset = TipoPeriodista.objects.all()
    serializer_class = TipoPeriodistaSerializers
    renderer_classes = [JSONRenderer]

class PeriodistaViewset(viewsets.ModelViewSet):
    queryset = Periodista.objects.all()
    serializer_class = PeriodistaSerializers
    renderer_classes = [JSONRenderer]

class TipoNoticiaSerializers(viewsets.ModelViewSet):
    queryset = TipoNoticia.objects.all()
    serializer_class = TipoNoticiaSerializers
    renderer_classes = [JSONRenderer]

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializers
    renderer_classes = [JSONRenderer]

# Create your views here.
def base(request):
    queryset = request.GET.get("buscar")
    noticias = Noticia.objects.all()
    periodistas = Periodista.objects.all()
    
    if queryset:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(TipoNoticia__icontains=queryset)
        ).distinct()
        
        periodistas = Periodista.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(rut__icontains=queryset)
        ).distinct()
        
    context = {
        'noticias': noticias,
        'periodistas': periodistas
    }    
    return render(request, 'core/base.html', context)

def index(request):
    noticia = Noticia.objects.order_by('-fecha')[:2]
    noti = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista': noticia,
        'noti': noti,
        'listafiltrada': periodista

    }
    return render(request, 'core/index.html',aux)

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            #AL USUARIO LE ASIGNAMOS UN GRUPO
            group = Group.objects.get(name='usuario')
            user.groups.add(group)
            #mensaje
            messages.success(request,'Usuario registrado correctamente!')
            #opcional (autentifa y logea al usuario)
            user = authenticate(username=formulario.cleaned_data['username'] ,password=formulario.cleaned_data['password1'])
            login(request, user)
            #redirecciona
            return redirect(to="index")         
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo registrar el usuario!')
    
    return render(request, 'registration/register.html', aux)

def contact(request):
    return render(request,'core/contact.html')

def espectaculo(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista': noticia,
        'listafiltrada': periodista

    }
    return render(request, 'core/espectaculo.html', aux)

def internacional(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista': noticia,
        'listafiltrada': periodista
        
    }
    return render(request, 'core/internacional.html', aux)

def nacional(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista': noticia,
        'listafiltrada': periodista
        
    }
    return render(request, 'core/nacional.html', aux)

def informatica(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista': noticia,
        'listafiltrada': periodista
        
    }
    return render(request, 'core/informatica.html', aux)

# CRUD PERIODISTA:
@permission_required('core.view_periodista')
def periodista(request):
    periodista = Periodista.objects.all()
    aux = {
        'listas' : periodista
    }

    return render(request,'core/periodista/index.html', aux)

@permission_required('core.add_periodista')
def periodistaadd(request):
    aux = {
        'form': PeriodistaForm()
    }

    if request.method == 'POST':
        formulario = PeriodistaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Periodista almacenado correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo almacenar al periodista!')

    return render(request,'core/periodista/crud/add.html' , aux)

@permission_required('core.change_periodista')
def periodistaupdate(request, id):
    periodista = Periodista.objects.get(id=id)
    aux = {
        'form': PeriodistaForm(instance=periodista)
    }

    if request.method == 'POST':
        formulario = PeriodistaForm(data=request.POST,instance=periodista)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,'Periodista modificado correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo modificar el periodista!')


    return render(request,'core/periodista/crud/update.html', aux)

@permission_required('core.delete_periodista')
def periodistadelete(request, id):
    periodista = Periodista.objects.get(id=id)
    periodista.delete()

    return redirect(to="periodista")

# CRUD NOTICIA:

@permission_required('core.view_noticia')
def noticia(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista' : noticia,
        'lista2': periodista
    }
    return render(request,'core/noticia/index.html', aux)

@permission_required('core.add_noticia')
def noticiadd(request):
    aux = {
        'form': NoticiaForm()
    }

    if request.method == 'POST':
        formulario = NoticiaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'La noticia fue enviada al administrador!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo almacenar la noticia!')

    return render(request,'core/noticia/crud/add.html' , aux)

@permission_required('core.change_noticia')
def noticiaupdate(request, id):
    noticia = Noticia.objects.get(id=id)
    aux = {
        'form': NoticiaForm(instance=noticia)
    }
    
    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST,instance=noticia)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,'Noticia modificada correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo modificar la noticia!')
            
    return render(request, 'core/noticia/crud/update.html',aux)

@permission_required('core.delete_noticia')
def noticiadelete(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    
    return redirect(to="noticia")

@permission_required('core.view_noticia')
def solicitudes(request):
    noticia = Noticia.objects.all()
    periodista = Periodista.objects.all()
    aux = {
        'lista' : noticia,
        'lista2': periodista
    }
    return render(request,'core/solicitudes.html', aux)

@permission_required('core.change_noticia')
def solicitudupdate(request, id):
    noticia = Noticia.objects.get(id=id)
    aux = {
        'form': NoticiaPeriodistaForm(instance=noticia)
    }
    
    if request.method == 'POST':
        formulario = NoticiaPeriodistaForm(data=request.POST,instance=noticia)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request,'Noticia modificada correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo modificar la noticia!')
            
    return render(request, 'core/solicitudupdate.html',aux)

@permission_required('core.add_noticia')
def solicitudadd(request):
    aux = {
        'form': NoticiaPeriodistaaddForm()
    }

    if request.method == 'POST':
        formulario = NoticiaPeriodistaaddForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'La noticia fue enviada al administrador!')
        else:
            aux['form'] = formulario
            messages.error(request,'No se pudo almacenar la noticia!')

    return render(request,'core/solicitudadd.html' , aux)

def solidelete(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    
    return redirect(to="solicitudes")

def account_locked(request):
    return render(request,'core/account_locked.html')

def servicios(request):
    return render(request,'core/servicios.html')

def dolarapi(request):
    return render(request,'core/apidolar/dolarapi.html')