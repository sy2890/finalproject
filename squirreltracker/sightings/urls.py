from . import views
from django.urls import path

urlpatterns = [
        path('',views.sightings),
        path('add/',views.add),
        ]
