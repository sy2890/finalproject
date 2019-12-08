from django.shortcuts import render
from django.http import Http404
from sightings.models import Squirrel

def map(request):
    squirrels = Squirrel.object.all()[:100]
    return render(request,'map/map.html',{'squirrels' = squirrels})


# Create your views here.
