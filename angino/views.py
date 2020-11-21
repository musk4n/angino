from django.shortcuts import render,redirect
from .models import * 
from .forms import * 

#rendoring home page
def home(request):
     return render(request, 'home.html')

def predictor(request):
    return render(request, 'predictor.html')

def tutorial(request):
    return render(request, 'tutorial.html')

# def forum(request):
#      return render(request, 'forum.html')

def measures(request):
    return render(request, 'measures.html')

def result(request):
    name=request.GET.get("fname")
    result_dict={"name":name}
    return render(request, 'result.html',result_dict)

def anonforum(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'forum.html',context)
 
def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)

