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
        'title': 'Projeto LMS: CURSOS'
    }
    return render(request, "detalhecurso.html", context)

def disciplina(request):
    conxtet = {
        'title': 'Projeto LMS: DISCIPLINAS'
    }
    return render(request, "disciplina.html", conxtet)