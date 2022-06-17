from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from AppCoder.models import Familia

# Create your views here.

def familia(self):
    
    familia1 = Familia(nombre= "Natalia", relacion = "Madre", edad = "43", nacimiento = "1978-05-10")
    familia1.save()

    familia2 = Familia(nombre= "Pablo", relacion = "Papá", edad = "44", nacimiento = "1977-03-20")
    familia2.save()

    familia3 = Familia(nombre= "Lara", relacion = "Hermana", edad = "10", nacimiento = "2012-02-04")
    familia3.save()

    documento = f"Mi familiar {familia1.relacion} se llama {familia1.nombre}, nacio el {familia1.nacimiento} y tiene {familia1.edad} años.\n Mi familiar {familia2.relacion} se llama {familia2.nombre}, nacio el {familia2.nacimiento} y tiene {familia2.edad} años.\n Mi familiar {familia3.relacion} se llama {familia3.nombre}, nacio el {familia3.nacimiento} y tiene {familia3.edad} años."

    return HttpResponse(documento)

def template1(self):
    miHtml = open("C:/Users/blas0/Desktop/PAGINA/ProyectoCoder/html/template.html")

    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
