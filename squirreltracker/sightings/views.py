from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SightingsForm
from .models import Squirrel

def sightings(request):
    if request.method == "GET":
        lst = Squirrel.objects.all()
        return render(request,'sightings/sightingsList.html',{'lst':lst})

def add(request):
    if request.method == 'POST':
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/add")
    else:
        form = SightingsForm()
    return render(request,'sightings/addSightings.html',{'form':form})


