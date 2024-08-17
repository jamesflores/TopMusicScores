from django.core.management.base import BaseCommand
from django.utils.text import slugify
from app.models import NewsItem, SheetMusic
import random
from datetime import timedelta, date
import marvin
from django.conf import settings
from pydantic import BaseModel


class BlogPost(BaseModel):
    title: str
    content: str


class Command(BaseCommand):
    help = 'Generates a news item on a randomly selected product'

    def handle(self, *args, **options):
        marvin.settings.openai.api_key = settings.MARVIN_OPENAI_API_KEY
        marvin.settings.openai.chat.completions.model = 'gpt-4o-mini'

        # get a random product
        product = SheetMusic.objects.order_by('?').first()

        # generate a blog post
        blog_posts = marvin.generate(n=1, target=BlogPost, instructions=f"""
            You are an expert copywriter for a music blog.
            Write a blog post about "{product.title}" by "{product.artist}" available for 
            instruments "{product.instruments}". The price of the product is ${product.list_price}.
            The product is described as "{product.description}". Given the genre of "{product.genres}", 
            write a blog post that will entice readers to purchase this product with approximately 300-500 quality words.
            """
        )
        blog_post = blog_posts[0]

        # save to the database
        news_item = NewsItem.objects.create(
            title=blog_post.title,
            title_slug=slugify(blog_post.title),
            author="marvin",
            content=blog_post.content,
            related_product=product
        )
