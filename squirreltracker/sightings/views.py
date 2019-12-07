from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SightingsForm
from .models import Squirrel

def sightings(request):
    if request.method == "GET":
        lst = Squirrel.objects.all()
        return render(request,'sightings/sightingsList.html',{'lst':lst})

class  addSightings(CreateView):
    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')

def edit_view(request, squirrel_id):
    instance = get_object_or_404(Squirrel, unique_squirrel_id=squirrel_id)
    form = SightingsForm(request.Post or None, instance=inistance)
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/{squirrel_id}')

    context ={
            'form':form,
            'sqid':squirrel_id,
            }
    return render(request, 'sightings/sightings_edit.html', context)

