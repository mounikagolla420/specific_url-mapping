from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mouni(request):
    return HttpResponse('<h1>she is psycho girl</h1>')

def sari(request):
    return HttpResponse('<h1>she is lovely sister</h1>')
