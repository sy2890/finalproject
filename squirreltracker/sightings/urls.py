from . import views
from django.urls import path

app_name = 'sightings'

urlpatterns = [
        path('',views.sightings,name = 'sighitngs'),
        path('add/',views.add,name = 'add'),
        path('<str:squirrel_id>/',views.update,name = 'update'),
        ]
