from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    data = {'tagline':'Actionable Real Time Intelligence'}
    return render(request, 'home.html', 
                  {'tagline':'Actionable Real Time Intelligence'})
