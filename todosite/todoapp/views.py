from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    task_list=Task.objects.all()
    return render(request,'todoapp/index.html',{'tasks':task_list})