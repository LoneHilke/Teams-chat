from django.shortcuts import render

# Create your views here.
from .models import Todo

# Rendering home page
def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/index.html', {'todos': todos})

def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    beskriv = request.POST.get('beskriv')
    todo = Todo.objects.create(beskriv=beskriv)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})

# Marking completed True
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})


#from: https://medium.com/@devsumitg/simple-todo-list-app-in-django-framework-htmx-bootstrap-5-8b68cbd47a1a