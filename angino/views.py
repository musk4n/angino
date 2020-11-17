from django.shortcuts import render 
from django.shortcuts import render 

#rendoring home page
def home(request):
     return render(request, 'home.html')

def predictor(request):
    return render(request, 'predictor.html')

