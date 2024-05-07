from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genres, name='genres'),
    path('genre/<str:genre_name>/', views.genre_detail, name='genre_detail'),
    path('publishers/', views.publishers, name='publishers'),
    path('publisher/<str:publisher_name>/', views.publisher_detail, name='publisher_detail'),
    path('instruments/', views.instruments, name='instruments'),
    path('instrument/<str:instrument_name>/', views.instrument_detail, name='instrument_detail'),
    path('product/<int:product_id>/', views.product_view, name='product'),
    path('search/', views.search_results, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
