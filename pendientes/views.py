from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea


# Create your views here.

def index(request):
        listita = Tarea.objects.all()# consultamos la BD y guardamos todo
                                      # los registros de la tabla
                                      # como objetos y guardamos en listita

        persona= {
           "nombre": "Mabel",
           "edad": 24,
           "hobbies":["bailar","comer","cantar","cocinar"],
           "lista_tareas" : listita ,
        }

        return render(request,"inicio.html",persona) 
    #saludo = "<h1>Hola, Mundo! </h1> Esta es la raiz /!!!!!"
    ##return HttpResponse(saludo) #retornamos el saludo

def tarea(request):
    return HttpResponse("Hola soy la vista tarea")

def vista_tareas(request):
        vista="<h1> Cree una lista tarea!! </h1> esta es la funcion"
        return HttpResponse(vista)

#crear la vista/funcion tarea y conectar con la direccion
# /tareas en el archivo urls.py
# despues ir al navegador y abrir http:..../tareas

# Crear una vista respuestas que retorne un texto cuando
# en el navegador entremos a http:...../info
# pista crear la funcion/vista en views.py y conectar en
# urls.py usando path(....)


def vista_respuestas(request):
        vista="<h1> Si, cree una vista repuestas!!!</h1> esta es la funcion"
        return HttpResponse(vista)
