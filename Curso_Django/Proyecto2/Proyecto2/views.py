"""
Django 
"""

from django.http import HttpResponse

def saludo(request): # primera vista
    return HttpResponse("Hola mundo. Primera página con Django")