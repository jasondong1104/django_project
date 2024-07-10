from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return HttpResponse('Rango app say hello to you!<br/><a href="/rango/about/">About</a>')
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse('This is a about info.<a href="/rango/">Index</a>')