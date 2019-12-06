from django.db import models

class Squirrel(models.Model):
    x = models.DecimalField(max_digits=20, decimal_places=14, null=True)
    y = models.DecimalField(max_digits=20, decimal_places=14, null=True)
    unique_squirrel_id = models.CharField(max_length=20, null=True)
    hectare = models.CharField(max_length=15, null=True)
    shift = models.CharField(max_length=10, null=True)
    date = models.DateField()
    hectare_squirrel_number = models.IntegerField()
    age = models.CharField(max_length=10,null=True)
    primary_fur_color = models.CharField(max_length=15, null=True)
    highlight_fur_color = models.CharField(max_length=15, null=True)
    combination_of_primary_and_highlight_color = models.CharField(
            max_length=100,
            null=True)
    color_notes = models.CharField(max_length=200, null=True)
    locatin = models.CharField(max_length=20, null=True)
    above_ground_sighter_measurement = models.CharField(max_length=10, null=True)
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
