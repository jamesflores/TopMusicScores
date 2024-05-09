from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl import connections


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        if settings.ELASTICSEARCH_URL:
            connections.create_connection(
                alias='default',
                hosts=[settings.ELASTICSEARCH_URL],
                timeout=20,
                use_ssl=True,
                verify_certs=True
            )