import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from ...models import Localisation


class Command(BaseCommand):
    help = "Load data from communes d'iles de france labellisées villes et villages fleuris 2016"

    def handle(self, *args, **options):
        data_file = settings.BASE_DIR / 'data' / 'communes-dile-de-france-labellisees-villes-et-villages-fleuris-2016.csv'
        keys = (
            "mairie", "label_vvf", "adresse_2", "departement", "libgeo",
            "code_postal", "ville", "longitude", "latitude", "mairie",
                )

        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            for row in reader:
                latitude, longitude = map(float, row['wgs84'].split(','))
                row['latitude'] = latitude
                row['longitude'] = longitude
                records.append({k: row[k] for k in keys})

        # add the data to the database
        for record in records:
            Localisation.objects.get_or_create(
                mairie=record['mairie'],
                ville=record['ville'],
                adresse=record['adresse_2'],
                code_postal=record['code_postal'],
                departement=record['departement'],
                longitude=record['longitude'],
                latitude=record['latitude'],
                label_vvf=record['label_vvf'],
            )
