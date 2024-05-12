import csv
from django.core.management.base import BaseCommand, CommandError
from app.models import SheetMusic
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = 'Imports the SMP affiliate data feed (tab-separated file)'

    def add_arguments(self, parser):
        parser.add_argument('tsv_file', type=str, help='The tab-separated file path')
        parser.add_argument('affiliate_id', type=int, help='Your affiliate ID')

    def handle(self, *args, **options):
        # clear existing data
        SheetMusic.objects.all().delete()

        file_path = options['tsv_file']
        try:
            with open(file_path, newline='', encoding='utf-8') as tsvfile:
                reader = csv.DictReader(tsvfile, delimiter='\t')
                for row in reader:
                    next(reader)  # skip header row
                    try:
                        seo_url = row['seo-url'].replace('000000', str(options['affiliate_id']))
                        SheetMusic.objects.create(
                            # rank	seo-url	cover-url	title	artist	instruments	format	genres	lead-time	list-price	publisher	isbn	item_type	description
                            rank=float(row['rank']),
                            item_url=seo_url,
                            cover_url=row['cover-url'],
                            title=row['title'],
                            title_slug=slugify(row['title']) + '-' + str(random.randint(10000, 99999)),
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
                        print(f'Imported {row["title"]} ({seo_url})')
                    except Exception as e:
                        print(f'Error importing {row["title"]}: {e}')

                self.stdout.write(self.style.SUCCESS('Successfully imported sheet music data'))
        except Exception as e:
            raise CommandError(f'Error importing data: {e}')
