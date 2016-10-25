from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
    """
    Hello world <br>
    <a href='about/'>about page</a>
    """
    )

def about(request):
    return HttpResponse("""Rango says here is the about page""")
