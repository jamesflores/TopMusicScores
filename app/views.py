from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import SheetMusic
from django.shortcuts import get_object_or_404
from django.db.models import Q


def home(request):
    sheet_music = SheetMusic.objects.all().order_by('-rank')
    paginator = Paginator(sheet_music, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'smp/home.html', {
        'page_obj': page_obj
    })


def product_view(request, title_slug):
    product = get_object_or_404(SheetMusic, title_slug=title_slug)
    upsell_products = SheetMusic.objects.exclude(title_slug=title_slug).order_by('?')[:8]
    return render(request, 'smp/product_detail.html', {
        'product': product,
        'upsell_products': upsell_products
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
        'results': queryset if query else None
    })
