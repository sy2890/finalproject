from django.db import models

class Squirrel(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=14, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=14, null=True)
    unique_squirrel_id = models.CharField(max_length=20, null=True)
    shift = models.CharField(max_length=10, null=True)
    date = models.DateField()
    age = models.CharField(max_length=10,null=True)
    primary_fur_color = models.CharField(max_length=15, null=True)
    locatin = models.CharField(max_length=20, null=True)
    specific_location = models.CharField(max_length=200, null=True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=200, null=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    


 

# Create your models here.
