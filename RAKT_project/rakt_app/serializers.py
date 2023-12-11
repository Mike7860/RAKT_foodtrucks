from rest_framework import serializers
from .models import FoodTruck


#foodtruck serializer
class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = ['name', 'latitude', 'longitude', 'description']
