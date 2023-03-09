from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kalpana(request):
    return HttpResponse('<h1>she is cute</h1>')

def supri(request):
    return HttpResponse('<h1>she is good</h1>')