from django.shortcuts import render
from django.http import HttpResponse


def index(request, usuario):
    
    return HttpResponse(f'Hola mundo {usuario}')

def home(request):
    return HttpResponse('hola perros')


# dato importante que acabo de descubrir JAJAJJA (no se si esto es real o no)
# pero si el parametro que recibe en la funcion se llama diferente a como lo pides
# en la url, django no lo reconoce como un parametro de la url
def saludar(request, nombre):
    return HttpResponse(f'Hola {nombre}')