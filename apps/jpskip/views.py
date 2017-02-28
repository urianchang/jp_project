from django.shortcuts import render, redirect
from .models import Character

# Create your views here.
def index(request):
    context = {
        'characters': Character.objects.all()[0]
    }
    return render(request, 'jpskip/index.html', context)

def process(request):
    print "***SUBMIT***"
    return redirect('/')
