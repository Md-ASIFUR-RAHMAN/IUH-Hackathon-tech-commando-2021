from django.db import models

# Create your models here.
class venue_details(models.Model):
    name = models.CharField(max_length=60)
    Wifi = models.CharField(max_length=30)
    date = models.DateField()
    capecity = models.IntegerField()
    cost = models.IntegerField()
    avalaible = models.CharField(max_length=50)
    Discription = models.CharField(max_length=100)