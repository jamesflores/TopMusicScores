import csv
from django.core.management.base import BaseCommand, CommandError
from app.models import SheetMusic

class Command(BaseCommand):
    help = 'Imports sheet music data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file path')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    SheetMusic.objects.create(
                        rank=float(row['rank']),
                        item_url=row['item-url'],
                        cover_url=row['cover-url'],
                        title=row['title'],
                        artist=row['artist'],
                        instruments=row['instruments'],
                        format=row['format'],
                        genres=row['genres'],
                        lead_time=row['lead-time'],
                        list_price=float(row['list-price']),
                        publisher=row['publisher'],
                        isbn=row['isbn'],
                        item_type=row['item_type'],
                        description=row['description']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully imported sheet music data'))
        except Exception as e:
            raise CommandError(f'Error importing data: {e}')
