from django.http.request import HttpRequest
from django.shortcuts import render
from cs3300_project.forms import HorseForm

from cs3300_project.models import Horse

# Create your views here.
def index(request: HttpRequest):
    context = {
        'horses': Horse.objects.all(),
        'active': 'Home'
    }
    return render(request, 'cs3300_project/index.html', context)

def horse(request: HttpRequest, horse_id):
    context = {
        'horse': Horse.objects.get(id=horse_id)
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
        'active': 'Add Horse'
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
        'active': 'Edit Horse'
    }
    return render(request, 'cs3300_project/edit_horse.html', context)

def delete_horse(request: HttpRequest, horse_id):
    Horse.objects.get(id=horse_id).delete()
    return index(request)

def pedigree(request: HttpRequest, horse_id):
    context = {
        'horse': Horse.objects.get(id=horse_id)
    }
    return render(request, 'cs3300_project/pedigree.html', context)