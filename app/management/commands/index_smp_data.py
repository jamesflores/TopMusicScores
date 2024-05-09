from elasticsearch_dsl import connections
from django.core.management.base import BaseCommand
from app.models import SheetMusic
from elasticsearch.helpers import bulk

from smp import settings


class Command(BaseCommand):
    help = 'Indexes all sheet music records to Elasticsearch'

    def handle(self, *args, **options):
        client = connections.get_connection()

        index_name = settings.ELASTICSEARCH_INDEX
        if client.indices.exists(index_name):
            client.indices.delete(index_name)

        client.indices.create(index_name)

        sheet_music = SheetMusic.objects.all()
        actions = []
        for product in sheet_music:
            action = {
                "_index": index_name,
                "_id": product.id,
                "_source": {
                    "rank": product.rank,
                    "item_url": product.item_url,
                    "cover_url": product.cover_url,
                    "title": product.title,
                    "title_slug": product.title_slug,
                    "artist": product.artist,
                    "instruments": product.instruments,
                    "format": product.format,
                    "genres": product.genres,
                    "lead_time": product.lead_time,
                    "list_price": product.list_price,
                    "publisher": product.publisher,
                    "isbn": product.isbn,
                    "item_type": product.item_type,
                    "description": product.description,
                    "full_search": f'{product.title} {product.artist} {product.instruments} {product.format} {product.genres} {product.publisher} {product.isbn} {product.item_type} {product.description}'
                }
            }
            actions.append(action)
            print(f'Indexing {product.title}')

        successes, _ = bulk(client, actions)
        self.stdout.write(self.style.SUCCESS(f'Indexed {successes} products'))