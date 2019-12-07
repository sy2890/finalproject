from django.shortcuts import render

from .models import Squirrel
def sightings(request):
    if request.method == "GET":
        lst = Squirrel.objects.all()
        return render(request,'sightings/sightingsList.html',{'lst':lst})
def add(request):
    if quest.method=="GET":
        return render(request,'addSightings.html')
    else:
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        unique_squirrel_id = request.POST.get("unique_squirrel_id")
        shift = request.POST.get("shift")
        date = request.POST.get("date")
        age = request.POST.get("age")
        primary_fur_color = request.POST.get("primary_fur_color")                       location = request.POST.get("location")
        specific_location = request.POST.get("specific_location")
        running = request.POST.get("running")
        chasing = request.POST.get("chasing")                                           climbing = request.POST.get("climbing")                                         eating = request.POST.get("eating")
        foraging = request.POST.get("foraging")                                         other_activities = request.POST.get("other_activities")                         kuks = request.POST.get("kuks")
        quaas = request.POST.get("quaas")
        moans = request.POST.get("moans")
        tail_flags = request.POST.get("tail_flags")
        tail_twitches = request.POST.get("tail_twitches")
        approaches = request.POST.get("approaches")
        indifferent = request.POST.get("indifferent")
        runs_from = request.POST.get("runs_from")
        squirrel=Squirrel(x=latitude,y=longitude,unique_squirrel_id=unique_squirrel_id,shift=shift,date=date,age=age,primary_fur_color=primary_fur_color,
        location=location,specific_location=specific_location,running=running,chasing=chasing,climbing=climbing,eating=eating,
        foraging=foraging,other_activities=other_activities,kuks=kuks,quaas=quaas,moans=moans,tail_flags=tail_flags,tail_twitches=tail_twitches,
        approaches=approaches,indifferent=indifferent,runs_from=runs_from)
        squirrel.save()
        return redirect("/sightings/")
