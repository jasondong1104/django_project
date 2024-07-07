from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Rango app say hello to you!<br/><a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse('This is a about info.<a href="/rango/">Index</a>')