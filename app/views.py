from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import SheetMusic
from django.shortcuts import get_object_or_404


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