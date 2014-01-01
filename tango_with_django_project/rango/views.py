# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says: Hello world! <a href='about/'>About</a>")

def about(request):
    #return HttpResponse("<a href="/rango/">Index</a>")
    return HttpResponse("Hello world <a href='/rango/'>Index</a>")