#shebang
# PROGRAMADO CON ATOM.


from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido



def saludo(request): # PRIMERA VISTA.
    pers1=Persona("arturo", "pérez")
    #nombre="Arturo"
    #apellido="Pérez"
    temas_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora=datetime.datetime.now()
#    doc_externo=open("/home/arturo/COMPARTIDA2/Desarrollo/Django\
#/Curso_Django/Proyecto3/Proyecto3/Plantillas/primera_plantilla.html")
#    plant=Template(doc_externo.read())
#    doc_externo.close()
##    doc_externo=loader.get_template('primera_plantilla.html')
#    contexto=Context({
#        "nombre_persona":pers1.nombre.capitalize(),
#        "apellido_persona":pers1.apellido.capitalize(),
#        "momento_actual":ahora,
#        "temas":temas_curso
#    })
##    documento=doc_externo.render({
##        "nombre_persona":pers1.nombre.capitalize(),
##        "apellido_persona":pers1.apellido.capitalize(),
##        "momento_actual":ahora,
##        "temas":temas_curso
##    })

##    return HttpResponse(documento)
    return render(request, "primera_plantilla.html", {
        "nombre_persona":pers1.nombre.capitalize(),
        "apellido_persona":pers1.apellido.capitalize(),
        "momento_actual":ahora,
        "temas":temas_curso
    })


def curso_c(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoC.html", {"damefecha":fecha_actual})

def curso_css(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "curso_css.html", {"damefecha":fecha_actual})

def despedida(request):
    return HttpResponse("Hasta luego cocodrilo.")

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body>Hola Mundo.

    <h1>Fecha y hora.</h1>

    Acá se los dejo. %s
    <body><html>
    """ % fecha_actual
    return HttpResponse(documento)

def calcula_edad(request, edad, anio):

    periodo=anio-2021
    edad_futura=edad+periodo
    documento="""<html><body>Hola.

    <h1>Vamos a calcular la edad.</h1>

    En el año %s tendrás %s años"
    <body><html>
    """ %(anio, edad_futura)

    return HttpResponse(documento)
