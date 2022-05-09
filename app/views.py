from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm,UpdateTaskForm
# Create your views here.
def index(request):
    todos=Task.objects.all()
    count_todos=todos.count()

    completed_todo=Task.objects.filter(complete=True)
    count_completed_todo=completed_todo.count()

    uncompleted_todo=count_todos-count_completed_todo

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm()
    contenx={
        'todo':todos,
        'form':form,
        'count_todo':count_todos,
        'count_completed_todo':count_completed_todo,
        'uncompleted_todo':uncompleted_todo,
        }
    return render(request,'app/index.html',contenx)

def update(request,pk):
    todo=Task.objects.get(id=pk)
    if request.method=='POST':
        form=UpdateTaskForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UpdateTaskForm(instance=todo)
    context={
        'form':form
    }
    return render(request,'app/update.html',context)


def delete(request,pk):
    todo=Task.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    
    return render(request,'app/delete.html')