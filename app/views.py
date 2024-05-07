from django.shortcuts import render
from app.models import SheetMusic


def home(request):
    return render(request, 'smp/home.html')


def genres(request):
    return render(request, 'smp/genres.html')


def genre_detail(request, genre_name):
    return render(request, 'smp/genre_detail.html', {'genre_name': genre_name})


def publishers(request):
    return render(request, 'smp/publishers.html')


def publisher_detail(request, publisher_name):
    return render(request, 'smp/publisher_detail.html', {'publisher_name': publisher_name})


def instruments(request):
    return render(request, 'smp/instruments.html')


def instrument_detail(request, instrument_name):
    return render(request, 'smp/instrument_detail.html', {'instrument_name': instrument_name})


def product_view(request, product_id):
    product = SheetMusic.objects.get(pk=product_id)
    context = {}
    context['product'] = product
    return render(request, 'smp/product_detail.html', context)


def search_results(request):
    return render(request, 'smp/search_results.html')


def about(request):
    return render(request, 'smp/about.html')


def contact(request):
    return render(request, 'smp/contact.html')