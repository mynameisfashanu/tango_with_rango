from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'rango/index.html',{'boldmessage' : "I am cool"})

def about(request):
    return render(request,'rango/about.html',{'message' : 'We love you!'})
