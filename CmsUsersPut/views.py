from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
#SuperUser: yes - yes


def Users(request, recurso):

    salida = ""
    if request.user.is_authenticated():
        salida += "You're inside " + request.user.username + "!"
        salida += "<a href='/admin/logout/'>Logout</a><br>"
    else:
        salida += "Please, put your login!"
        salida += "<a href='/admin/login/'>Login</a><br>"


    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            return HttpResponse(salida + fila.page)
        except Page.DoesNotExist:
            return HttpResponseNotFound(salida)

    elif request.method == "PUT":
        if request.user.is_authenticated():
            try:
                body = request.body
                fila = Page.objects.create(name=recurso, page=cuerpo)
                fila.save()
                return HttpResponse("Fila creada!")
            except:
                return HttpResponseNotFound("Hazlo bien!")
            else:
                return HttpResponseNotFound("No puedes modificarlo")

