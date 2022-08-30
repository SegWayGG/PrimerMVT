from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .models import Familiares

def familia(request):
    familiar1=Familiares(nombre="Andrea", edad=36, nacimiento="1986-06-21")
    familiar2=Familiares(nombre="Nestor", edad=38, nacimiento="1984-02-12")
    familiar3=Familiares(nombre="Tatiana", edad=23, nacimiento="1999-07-25")
    familiar4=Familiares(nombre="Sofia", edad=12, nacimiento="2010-05-03")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    diccionario={"familiar1":familiar1, "familiar2":familiar2, "familiar3":familiar3, "familiar4":familiar4}
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)