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
    if request.POST['step'] == "4":
        return redirect('/step4')
    if request.POST['step'] == "5":
        return redirect('/step5')
    return redirect('/')

def step4(request):
    return render(request, 'jpskip/step4.html', {'randomCat4': Character.objects.randomizer(4)})

def step5(request):
    return render(request, 'jpskip/step5.html', {'random': Character.objects.randomizer()})
