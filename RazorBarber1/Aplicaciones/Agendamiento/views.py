from django.shortcuts import render, redirect
from .models import Barbero, Rol 
# Create your views here.

def home(request):
    listadoBarberos = Barbero.objects.all() 
    return render(request, 'administrador/admin.html', {'barberos': listadoBarberos})

def administrador(request):
    listadoBarberos = Barbero.objects.all()
    return render(request, 'administrador/admin.html', {'barberos': listadoBarberos})

def perfilAdmin(request):
    return render(request, 'administrador/perfilAdmin')

def registroBarbero(request):
    idBarbero = request.POST.get('txtDocumento')
    nombre = request.POST.get('txtNombre')
    apellido = request.POST.get('txtApellido')
    correoE = request.POST.get('txtCorreo')
    clave = request.POST.get('txtContraseña')
    rol = Rol.objects.get(id=1)
    
    nuevoBarbero = Barbero(idBarbero = idBarbero, nombre = nombre, apellido = apellido, correoE = correoE,clave =clave, idRol = rol)
    
    nuevoBarbero.save()
    return redirect('/')

def administrador(request):
    listadoBarberos = Barbero.objects.all()
    return render(request, 'administrador/admin.html', {'barberos': listadoBarberos})