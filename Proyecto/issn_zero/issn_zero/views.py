#! /usr/bin/python

from django.http import HttpResponse
import datetime
#from django.template import Template, Context #comprobar si necesario
#from django.template.loader import get_template
from django.shortcuts import render

class Usuario(object):
    def __init__(self, nombre, nick, contrasenia, titulo, email,\
quote, bio, inventario, saldo_isc, privacidad, config):
        self.nombre=nombre
        self.nick=nick
        self.contrasenia=contrasenia
        self.titulo=titulo
        self.email=email
        self.quote=quote
        self.bio=bio
        self.inventario=inventario
        self.saldo_isc=saldo_isc
        self.privacidad=privacidad
        self.config=config


def profile(request):
    pers1=Usuario(
        "arturo",
        "ilkhan",
        "1234",
        "supravicecontraalmirante de la flota hinchable hispalense.",
        "emailfalso@gobiernomundial.com",
        "Más vale pájaro en mano que caimán en las pelotas",
        "Un tío que iba por ahí y le pasaban cosas.",
        ["espada vorpalina +20 contra políticos", "escudo de chapa wena wena wena", "Vaselina"],
        10000000000,
        False,
        1
    )
    otros_datos=["Battletech", "Star Wars", "Star Trek", "Elite Dangerous", "Raised by Wolves"]
    ahora=datetime.datetime.now()

    todos_los_datos={ #diccionario que almacena todos los datos (pruebas).
        "nombre_profile":pers1.nombre.capitalize(),
        "nick_profile":pers1.nick.lower(),
        "contrasenia_profile":pers1.contrasenia,
        "titulo_profile":pers1.titulo.capitalize(),
        "email_profile":pers1.email,
        "quote_profile":pers1.quote,
        "bio_profile":pers1.bio,
        "inventario_profile":pers1.inventario,
        "saldo_isc_profile":pers1.saldo_isc,
        "privacidad_profile":pers1.privacidad,
        "config_profile":pers1.config,
        "momento_actual":ahora,
        "demas_datos":otros_datos
    }

    return render(request, "profile.html", {
        "nombre_profile":pers1.nombre.capitalize(),
        "nick_profile":pers1.nick.lower(),
        "contrasenia_profile":pers1.contrasenia,
        "titulo_profile":pers1.titulo.capitalize(),
        "email_profile":pers1.email,
        "quote_profile":pers1.quote,
        "bio_profile":pers1.bio,
        "inventario_profile":pers1.inventario,
        "saldo_isc_profile":pers1.saldo_isc,
        "privacidad_profile":pers1.privacidad,
        "config_profile":pers1.config,
        "momento_actual":ahora,
        "demas_datos":otros_datos,
        "todos_los_datos":todos_los_datos.items()
    })
