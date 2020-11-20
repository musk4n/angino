from django.shortcuts import render 
from django.shortcuts import render 

#rendoring home page
def home(request):
     return render(request, 'home.html')

def predictor(request):
    return render(request, 'predictor.html')

<<<<<<< HEAD
def result(request):
     # print(request.GET)
     return render(request, "result.html")
=======
def tutorial(request):
    return render(request, 'tutorial.html')

def forum(request):
    return render(request, 'forum.html')

def measures(request):
    return render(request, 'measures.html')

def result(request):
    return render(request, 'result.html')
>>>>>>> 5120816a3ae37c38ce97e24d3b8c2981a3d62791

