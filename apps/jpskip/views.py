from django.shortcuts import render, redirect
from .models import Character

# Create your views here.
def index(request):
    context = {
        'characters': Character.objects.all()
    }
    return render(request, 'jpskip/index.html', context)
