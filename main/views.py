from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from problem.models import Problem

# Create your views here.

def index(request):
    name='main/base.html'
    problems = Problem.objects.all()
    return render(request, 'main/index.html', {'template': name,
                                               'problems': problems,})
