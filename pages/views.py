from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from trello_app.models import Task, TaskList
# Create your views here.

def register(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  if request.method == 'POST':
    # form = UserCreationForm(data=request.POST)
    form = CreateUserForm(data=request.POST)
    if form.is_valid():
      form.save()
      # redirect to login page if successful
      return redirect('login')
  else:
    # form = UserCreationForm()
    form = CreateUserForm()
  # in case there are any errors, use the same form object
  return render(request, 'pages/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
  # get the lists and tasks associated with the user
  
  # ORM: Object Relational Mapping
  # Django provides a rich API
  # that allows us to query database using
  # python code and object
  
  user = request.user
  # lists = user.tasklist_set.all()
  lists = TaskList.objects.filter(user=user)
  tasks = Task.objects.filter(list__in=lists)
  return render(request, 'pages/dashboard.html', {'lists': lists, 'tasks': tasks})

def login(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  if request.method == 'POST':
    # if the user exists with given credentials
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      # login the user, associate the user with request
      auth_login(request, user)
      # redirect to dashboard
      return redirect('dashboard')
    else:
      # provide some error message over here
      messages.error(request, 'Username or password is incorrect')
  return render(request, 'pages/login.html')

def logout(request):
  # remove the user associated with the request
  auth_logout(request)
  return redirect('home')

def home(request):
  if request.user.is_authenticated:
    # if the user is logged in
    return redirect('dashboard')
  return render(request, 'pages/home.html')
  
