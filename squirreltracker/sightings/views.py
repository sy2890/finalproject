from django.shortcuts import render

from .models import Squirrel
def sightings(request):
    if request.method == "GET":
        lst = Squirrel.objects.all()
        return render(request,'sightings/sightingsList.html',{'lst':lst})
# Create your views here.
