from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from .models import FoodTruck
from django.shortcuts import render



#foodtruck view
class FoodTruckAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            latitude = float(request.query_params.get('latitude'))
            longitude = float(request.query_params.get('longitude'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid latitude or longitude'}, status=400)

        # Example query to get food trucks within a certain distance
        food_trucks = FoodTruck.objects.filter(
            location__distance_lte=(Point(longitude, latitude), D(m=1000))
        )

        # Serialize and return the data
        serialized_data = FoodTruckSerializer(food_trucks, many=True).data
        return Response(serialized_data)


#main view
def main_view(request):
    return render(request, 'index.html', context={'your_data': 'some_data'})