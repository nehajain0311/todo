from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def index(request):
    task_list=Task.objects.all()
    return render(request,'todoapp/index.html',{'tasks':task_list})

def add(request):
    
    return render(request,'todoapp/add.html')

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=="POST":
        task.delete()
        return redirect("/")
    return render(request,'todoapp/delete.html',{'task':task})