from django.db import models


#foodtruck model
class FoodTruck(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
