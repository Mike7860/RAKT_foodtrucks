import csv
import requests
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from rakt_app.models import FoodTruck


class Command(BaseCommand):
    help = 'Import food trucks from CSV'

    def handle(self, *args, **options):
        url = 'https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv'

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Error fetching CSV data: {e}'))
            return

        csv_data = response.text.splitlines()

        # Skip the header row
        csv_reader = csv.reader(csv_data[1:])
        for row in csv_reader:
            FoodTruck.objects.create(
                name=row[0],
                latitude=float(row[1]),
                longitude=float(row[2]),
                description=row[3]
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported food trucks'))
