from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import SightingsForm
from .models import Squirrel

def sightings(request):
    if request.method == "GET":
        sightings = Squirrel.objects.all()
        return render(request,'sightings/sightings.html',{'sightings':sightings})

def add(request):
    if request.method == 'POST':
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/add")
    else:
        form = SightingsForm()
    return render(request,'sightings/addSightings.html',{'form':form,})

def update(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_squirrel_id = squirrel_id)
    if request.method == 'POST':
        form = SightingsForm(request.POST,instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SightingsForm(instance = squirrel)
        context = {'form':form}
        return render(request,'sightings/updateSightings.html',context)

def stats(request):
    age_stats = Squirrel.objects.filter(age = 'Juvenile').count()
    primary_fur_col_stats = Squirrel.objects.filter(primary_fur_color = 'Gray').count()
    location_stats = Squirrel.objects.filter(location = 'Ground Plane').count()
    running_stats = Squirrel.objects.filter(running = 'True').count()
    chasing_stats = Squirrel.objects.filter(chasing = 'True').count()
    context = {
            'age':age_stats,
            'fur':primary_fur_col_stats,
            'location':location_stats,
            'running':running_stats,
            'chasing':chasing_stats,
            }
    return render(request,'sightings/statsSightings.html',context)




