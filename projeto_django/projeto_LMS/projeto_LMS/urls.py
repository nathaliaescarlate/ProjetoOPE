"""projeto_LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from core.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('detalhecurso/', detalhecurso, name="detalhedocurso"),
    path('disciplina/', disciplina, name="disciplina"),
    path('listacurso/', listacurso, name="listadocurso"),
    path('noticias/', noticias, name="noticias"),
    #url(r'^disciplina/$', index, name='index_d'),
    
]
