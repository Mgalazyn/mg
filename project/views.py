from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.

def project(request):
    context = {}
    return render(request, 'main.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def history(request):
    context = {}
    return render(request, 'history.html', context)


def loginpage(request):

    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
            messages.success(request, 'You are logged in')
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Username or password is incorrect')
            
    context = {}
    return render(request, 'login.html', context)


def logoutuser(request):
    logout(request)
    messages.error(request, 'User logout ')
    return redirect('login')


def iceland(request):
    context = {}
    return render(request, 'iceland.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User created successfully!')

            login(request, user)
            return redirect('main')

        else:
            messages.error(request, 'Something went wrong! ')

    context = {'form': form}
    return render(request, 'register.html', context)