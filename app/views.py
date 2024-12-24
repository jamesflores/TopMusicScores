import random
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from app.models import SheetMusic, NewsItem
from django.shortcuts import get_object_or_404
from django.db.models import Q


def home(request):
    order_by = request.GET.get('order_by', '-rank')  # default to popularity
    items_per_page = int(request.GET.get('items_per_page', 20))
    
    # Define valid ordering options
    valid_order_fields = {
        'rank': 'Popularity (Low to High)',
        '-rank': 'Popularity (High to Low)',
        'title': 'Title (A-Z)',
        '-title': 'Title (Z-A)',
        'artist': 'Artist (A-Z)',
        '-artist': 'Artist (Z-A)',
        'list_price': 'Price (Low to High)',
        '-list_price': 'Price (High to Low)',
    }
    
    # Define valid items per page options
    per_page_choices = [20, 50, 100, 200, 500]
    
    if order_by not in valid_order_fields:
        order_by = '-rank'
    
    if items_per_page not in per_page_choices:
        items_per_page = 20
    
    sheet_music = SheetMusic.objects.all().order_by(order_by)
    paginator = Paginator(sheet_music, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'smp/home.html', {
        'page_obj': page_obj,
        'rss_feed_url': reverse('news_feed'),
        'order_by': order_by,
        'valid_order_fields': valid_order_fields,
        'items_per_page': items_per_page,
        'per_page_choices': per_page_choices,
    })


def product_view(request, title_slug):
    product = get_object_or_404(SheetMusic, title_slug=title_slug)
    upsell_products = SheetMusic.objects.exclude(title_slug=title_slug).order_by('?')[:8]
    ad_images = [
        'https://assets.sheetmusicplus.com/banner/ezr/student/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/teacher/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/choir/CD_AF_250x250_v1.jpg',
    ]
    return render(request, 'smp/product_detail.html', {
        'product': product,
        'upsell_products': upsell_products,
        'ad_image': random.choice(ad_images),
        'rss_feed_url': reverse('news_feed')
    })


def about(request):
    return render(request, 'smp/about.html')


def search(request):
    query = request.GET.get('q')
    
    if query:
        query = query.strip()
        search_query = (
            Q(artist__icontains=query) |
            Q(title__icontains=query) |
            Q(instruments__icontains=query) |
            Q(genres__icontains=query) |
            Q(publisher__icontains=query) |
            Q(isbn__icontains=query) |
            Q(item_type__icontains=query) |
            Q(description__icontains=query)
        )
        queryset = SheetMusic.objects.filter(search_query).order_by('-rank')[:12]
    else:
        queryset = SheetMusic.objects.none()

    return render(request, 'smp/search.html', {
        'query': query,
        'results': queryset if query else None,
        'rss_feed_url': reverse('news_feed')
    })


def news(request):
    news_items = NewsItem.objects.all().order_by('-published')
    paginator = Paginator(news_items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ad_images = [
        'https://assets.sheetmusicplus.com/banner/ezr/student/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/teacher/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/choir/CD_AF_250x250_v1.jpg',
    ]
    return render(request, 'smp/news.html', {
        'page_obj': page_obj,
        'ad_image': random.choice(ad_images),
        'rss_feed_url': reverse('news_feed')
    })


def news_item(request, title_slug):
    news_item = get_object_or_404(NewsItem, title_slug=title_slug)
    upsell_products = SheetMusic.objects.exclude(title_slug=title_slug).order_by('?')[:8]
    ad_images = [
        'https://assets.sheetmusicplus.com/banner/ezr/student/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/teacher/featured_250x250.jpg',
        'https://assets.sheetmusicplus.com/banner/ezr/choir/CD_AF_250x250_v1.jpg',
    ]
    return render(request, 'smp/news_item.html', {
        'news_item': news_item,
        'product': news_item.related_product,
        'upsell_products': upsell_products,
        'ad_image': random.choice(ad_images),
        'rss_feed_url': reverse('news_feed')
    })