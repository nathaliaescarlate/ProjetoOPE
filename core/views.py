from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'title': 'Projeto LMS'
    }
    return render(request, "index.html", context)

def detalhecurso(request):
    context = {
        'title': 'Projeto LMS: DETALHE DOS CURSOS'
    }
    return render(request, "detalhecurso.html", context)

def disciplina(request):
    context = {
        'title': 'Projeto LMS: DISCIPLINAS'
    }
    return render(request, "disciplina.html", context)

def listacurso(request):
    context = {
        'title': 'Projeto LMS: LISTA DO CURSOS'
    }
    return render(request, "listacurso.html", context)

def noticias(request):
    context = {
        'title': 'Projeto LMS: NOTICIAS'
    }
    return render(request, "noticias.html", context)


