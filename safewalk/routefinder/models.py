from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, min_length=7)
    
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Crime(models.Model):
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    date = models.DateTimeField('date committed')
    link = models.CharField(max_length=100)

    def __str__(self):
        return "Lat: " + str(self.latitude) + " Long: " + str(self.longitude) + " " + str(self.date)