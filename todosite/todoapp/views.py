from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy



from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskCreateView(CreateView):
    model = Task
    template_name = 'todoapp/cbvadd.html'
    fields='__all__'
    success_url=reverse_lazy('todoapp:cbvindex')


#this function added to support the Listview Add component before CreateView Is generated later it is completely redundant andd not used anywhwere
def add(request):
    if request.method=='POST':
        text=request.POST.get('text')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(text=text,priority=priority,date=date)
        task.save()
        return redirect("/cbvindex/")
    return render(request,'todoapp/add.html')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todoapp/cbvdetail.html'
    context_object_name='task'

#this function is not used when taskdetailview is used from above
def detail(request,task_id):
    task=Task.objects.get(id=task_id)    
    return render(request,'todoapp/detail.html',{'task':task})

class TaskListView(ListView):
    model = Task
    template_name = "todoapp/cbvindex.html"
    #context_object_name='tasks'  #this should match the variable passed to template and used
    
    #below code is used to manipulate queryset
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books #odrder by is used to show highest priority on top
        #context key should match the template context name
        context['tasks'] = Task.objects.all().order_by('-priority').values
        return context

#this function serve same as above listview generic view with add function, detail function and not used after listview is used
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


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todoapp/cbvupdate.html"
    context_object_name='task'
    fields=("text","priority","date") #add fields that can be modified
    
    #redirect on success
    def get_success_url(self) -> str:   
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id}) #redirected to detailview with object id
    
#this method is not used when taskUpdate generic view is used    
def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if request.method=="POST":
        if form.is_valid():
            form.save()        #form is associated with model, so it will save model too
        return redirect("/")
    return render(request,'todoapp/update.html',{'form':form,'task':task})


class TaskDeleteView(DeleteView):
    model=Task
    template_name="todoapp/cbvdelete.html" 
    #context_object_name='task'
    success_url= reverse_lazy('todoapp:cbvindex') #redirected to deleteview with object id
    
 
 #this view is nolonger used when generic delete view is in use
def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=="POST":
        task.delete()
        return redirect("/")
    return render(request,'todoapp/delete.html',{'task':task})