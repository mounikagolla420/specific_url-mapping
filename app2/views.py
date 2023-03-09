from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vijji(request):
    return HttpResponse('<h1><marque>she is my buddy</marque></h1>')

def mahi(request):
    return HttpResponse('<h1>mahi is stright forward person</h1>')