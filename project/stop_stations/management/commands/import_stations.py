from django.core.management.base import BaseCommand

from stop_stations.models import Route, Station

import csv

class Command(BaseCommand):

    def handle(self, *args, **options):

        def parse_route(route: str):
            obj, _ = Route.objects.get_or_create(name=route)
            return obj

        with open('moscow_bus_stations.csv', encoding='cp1251', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for n, row in enumerate(reader):
                try:
                    obj, _ = Station.objects.update_or_create(
                        latitude=float(row['Latitude_WGS84']),
                        longitude=float(row['Longitude_WGS84']),
                        name=row['Name'],
                    )
                    obj.routes.set(tuple(map(parse_route, row['RouteNumbers'].split('; '))))
                    self.stdout.write(f'row #{n} OK')
                except (ValueError, KeyError) as error:
                    self.stdout.write(f'row #{n} {error}')
