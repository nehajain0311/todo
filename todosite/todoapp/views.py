from django.shortcuts import render,redirect


from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    task_list=Task.objects.all().order_by('-priority').values #sorted according to descending priority
    if request.method=='POST':
        text=request.POST.get('text')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(text=text,priority=priority,date=date)
        task.save()
        return redirect("/")
    return render(request,'todoapp/index.html',{'tasks':task_list})


def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if request.method=="POST":
        if form.is_valid():
            form.save()        #form is associated with model, so it will save model too
        return redirect("/")
    return render(request,'todoapp/update.html',{'form':form,'task':task})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=="POST":
        task.delete()
        return redirect("/")
    return render(request,'todoapp/delete.html',{'task':task})