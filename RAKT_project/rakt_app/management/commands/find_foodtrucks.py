from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rakt_app.models import FoodTruck


class Command(BaseCommand):
    help = 'Find nearby food trucks'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float)
        parser.add_argument('longitude', type=float)

    def handle(self, *args, **options):
        latitude = options['latitude']
        longitude = options['longitude']

        user_location = Point(longitude, latitude, srid=4326)

        food_trucks = FoodTruck.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')[:5]

        for truck in food_trucks:
            self.stdout.write(f'{truck.name} - {truck.description}')
