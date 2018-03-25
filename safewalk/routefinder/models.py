from django.db import models

# Create your models here.

class Crime(models.Model):
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    date = models.DateTimeField('date committed')

    def __str__(self):
        return "Lat: " + str(self.latitude) + " Long: " + str(self.longitude) + " " + str(self.date)