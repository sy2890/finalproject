from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from .models import Squirrel

def sightings(request):
    if request.method == "GET":
        lst = Squirrel.objects.all()
        return render(request,'sightings/sightingsList.html',{'lst':lst})

class  addSightings(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')
