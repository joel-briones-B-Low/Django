from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona, Usuario
from django.shortcuts import get_object_or_404, render
from .forms import formPersona
import os
from django.shortcuts import redirect



def index(request, usuario):
    usuario = list(Usuario.objects.filter(id_persona__nombre__contains='Joel').values())
    # por defecto el jsonresponse acepta diccionarios en caso de que tu le mandes
    # una lista o otro tipo de dato debes poner un safe=False
    
    return render(request, 'personas.html', {
        'usuario': usuario
    })

def listaPersonas(request):
    
    personas = Persona.objects.all()
    return render(request, 'lista_personas.html', {
        'personas': personas
    })

def home(request):
    return HttpResponse('hola perros')


# dato importante que acabo de descubrir JAJAJJA (no se si esto es real o no)
# pero si el parametro que recibe en la funcion se llama diferente a como lo pides
# en la url, django no lo reconoce como un parametro de la url
def saludar(request, id):
    # usuario = Usuario.objects.get(id=id)
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'usaurios.html',{
        'usuario': usuario
    })

def vista(request):
    datos = 'Hola perros'
    return render(request,'index.html', {
        'datos': datos
    })
    
def crearPersona(request):
    os.system('cls')
    print(request.method)
    if request.method == 'POST':
        os.system('cls')
        print(request.POST)
        print(request.POST['nombre'])
        print(request.POST['apellido'])
            
        persona = Persona.crear(nombre=request.POST['nombre'], apellido=request.POST['apellido'])
        persona.save()
        print(Persona.objects.all())
        return redirect('lista')
        
    elif request.method == 'GET':
        return render(request, 'crear_persona.html', {
            'form' : formPersona()
        })