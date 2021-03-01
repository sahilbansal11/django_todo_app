from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
# Create your views here.

def register(request):
  if request.method == 'POST':
    # form = UserCreationForm(data=request.POST)
    form = CreateUserForm(data=request.POST)
    if form.is_valid():
      form.save()
      # redirect to login page if successful
  else:
    # form = UserCreationForm()
    form = CreateUserForm()
  # in case there are any errors, use the same form object
  return render(request, 'pages/register.html', {'form': form})

def dashboard(request):
  # get the lists and tasks associated with the user
  return render(request, 'pages/dashboard.html')

def login(request):
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
  
