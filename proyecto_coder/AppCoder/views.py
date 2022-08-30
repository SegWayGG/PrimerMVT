from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .models import Curso


def probandohtml(request):
    nom = "Francisco"
    ape= "Santillan"
    lista=[8,5,6,4,8,9,2,1,3,7]
    diccionario={"nom":nom, "ape":ape, 'lista':lista}
    #Cargo Template
    plantilla=loader.get_template("template1.html")
    #Renderizo contexto (Que es un diccionario)
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def curso(request):
    curso=Curso(nombre="Python", comision=31105)
    curso2=Curso(nombre="JS", comision=21502)
    curso3=Curso(nombre="Django", comision=36840)
    curso.save()
    curso2.save()
    curso3.save()
    texto=f"Cursos Creados!, creamos uno de {curso.nombre}, uno de {curso2.nombre} y el ultimo es de {curso3.nombre}!"
    return HttpResponse(texto)