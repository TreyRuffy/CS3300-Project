from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Horse(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    long_description = models.TextField(max_length=10000)
    image = models.ImageField(null=True, blank=True)
    pedigree = models.ForeignKey('Pedigree', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class BuyableHorse(models.Model): 
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return self.horse.name + " - " + str(self.price)
    
class Pedigree(models.Model):
    sire = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='sire')
    dam = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='dam')
    def __str__(self):
        return "Sire: " + self.sire.name + " Dam: " + self.dam.name

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username