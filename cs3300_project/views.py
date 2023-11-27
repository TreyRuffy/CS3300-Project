from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cs3300_project.forms import HorseForm

from .models import Horse, Account
from .forms import LoginForm

# Create your views here.
def index(request: HttpRequest):
    context = {
        'horses': Horse.objects.all(),
        'active': 'Home',
        'username': request.user
    }
    return render(request, 'cs3300_project/index.html', context)

def horse(request: HttpRequest, horse_id):
    context = {
        'horse': Horse.objects.get(id=horse_id),
        'username': request.user
    }
    return render(request, 'cs3300_project/horse.html', context)

def add_horse(request: HttpRequest):
    form = HorseForm()
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    context = {
        'form': form,
        'active': 'Add Horse',
        'username': request.user
    }
    return render(request, 'cs3300_project/edit_horse.html', context)

def edit_horse(request: HttpRequest, horse_id):
    form = HorseForm(instance=Horse.objects.get(id=horse_id))
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES, instance=Horse.objects.get(id=horse_id))
        if form.is_valid():
            form.save()
            return horse(request, horse_id)
    context = {
        'form': form,
        'project': Horse.objects.get(id=horse_id),
        'horse': Horse.objects.get(id=horse_id),
        'active': 'Edit Horse',
        'username': request.user
    }
    return render(request, 'cs3300_project/edit_horse.html', context)

@login_required(login_url='login')
def delete_horse(request: HttpRequest, horse_id):
    Horse.objects.get(id=horse_id).delete()
    return index(request)

def pedigree(request: HttpRequest, horse_id):
    context = {
        'horse': Horse.objects.get(id=horse_id),
        'username': request.user
    }
    return render(request, 'cs3300_project/pedigree.html', context)

def loginPage(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return index(request)
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')

    context = {
        'active': 'Login',
    }
    return render(request, 'cs3300_project/login.html', context)

@login_required(login_url='login')
def account(request: HttpRequest):
    context = {
        'active': 'Account',
        'username': request.user
    }
    return render(request, 'cs3300_project/account.html', context)

def register(request: HttpRequest):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    context = {
        'active': 'Register',
        'form': form,
    }
    return render(request, 'cs3300_project/register.html', context)

@login_required(login_url='login')
def logoutPage(request: HttpRequest):
    context = {
        'active': 'Logout',
    }
    logout(request)
    return render(request, 'cs3300_project/logout.html', context)