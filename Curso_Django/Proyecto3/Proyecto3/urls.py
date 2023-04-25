"""Proyecto3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto3.views import saludo, despedida,\
damefecha, calcula_edad, curso_c, curso_css

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urlsaludo/', saludo),
    path('urldespedida/', despedida),
    path('urlfecha/', damefecha),
    path('urledad/<int:edad>/<int:anio>', calcula_edad),
    path('cursoc/', curso_c),
    path('cursocss/', curso_css),
]
