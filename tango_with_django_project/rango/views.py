# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    #return HttpResponse("Rango says: Hello world! <a href='about/'>About</a>")
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    #return HttpResponse("<a href="/rango/">Index</a>")
    #return HttpResponse("Hello world <a href='/rango/'>Index</a>")
    context = RequestContext(request)
    context_dict = {'boldmessage': "Nous, le steak, on aime ça!"}
    return render_to_response('rango/about.html', context_dict, context)