from django.shortcuts import render, redirect
from .models import TaskList, Task
from .forms import TaskForm

# Create your views here.

def index(request):
  # this data is now comings from DB
  lists = TaskList.objects.all()
  tasks = Task.objects.all()
  return render(request, 'trello_app/index.html', {'lists': lists, 'tasks': tasks})

def create_list(request):
  if request.method == 'POST':
    # fetch the data and save it in the DB
    list_name = request.POST['list_name']
    list = TaskList(name=list_name)
    list.save()
    # return render(request, 'trello_app/new_list.html')
    return redirect('index')
  else:
    return render(request, 'trello_app/new_list.html')

def create_task(request):
  if request.method == 'POST':
    # fetch the data and save it in the DB
    form = TaskForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = TaskForm()
  
  # same form object will get rendered in case of error
  return render(request, 'trello_app/new_task.html', {'form': form})