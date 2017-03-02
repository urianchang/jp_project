from django.shortcuts import render, redirect
import random
from .models import Character

# Create your views here.
def index(request):
    context = {
        'characters': Character.objects.all()[0]
    }
    return render(request, 'jpskip/index.html', context)

def process(request):
    print "***SUBMIT***"

    if request.POST['step'] == "1":
        return redirect('/step1')
    if request.POST['step'] == "2":
        return redirect('/step2')
    if request.POST['step'] == "3":
        return redirect('/step3')
    if request.POST['step'] == "4":
        return redirect('/step4')
    if request.POST['step'] == "5":
        return redirect('/step5')
    return redirect('/')

def step1(request):
    return render(request, 'jpskip/step1.html', {'random': Character.objects.randomizer()})
def step2(request):
    return render(request, 'jpskip/step2.html', {'random': Character.objects.randomizer()})
def step3(request):
    return render(request, 'jpskip/step3.html', {'random': Character.objects.randomizer(random.randrange(1, 4))})
def step4(request):
    return render(request, 'jpskip/step4.html', {'randomCat4': Character.objects.randomizer(4)})
def step5(request):
    return render(request, 'jpskip/step5.html', {'random': Character.objects.randomizer()})
