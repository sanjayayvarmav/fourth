from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import TaskForm
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskUpdate(UpdateView):
    model =Task
    template_name ='edit.html'
    context_object_name ='task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class Taskdelete(DeleteView):
    model=Task
    template_name='delete.html'
    success_url = reverse_lazy('cbvhome')



class TaskList(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'sanjay'

def home(request):
    tasks = Task.objects.all()
    if request.method =='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'task':tasks})

def details(request):
    return render(request,'details.html')
def delete(request,taskid):

    if request.method == "POST":
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance= task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})