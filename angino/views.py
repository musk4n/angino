from django.shortcuts import render 
from django.shortcuts import render 

#rendoring home page
def home(request):
     return render(request, 'home.html')

def predictor(request):
    return render(request, 'predictor.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def forum(request):
    return render(request, 'forum.html')

def measures(request):
    return render(request, 'measures.html')
