from . import views
from django.urls import path

app_name = 'sightings'

urlpatterns = [
        path('',views.sightings,name = 'sighitngs'),
        path('add/',views.addSightings.as_view(),name = 'add'),
        ]
