from django.urls import path
from . import views
from app.feeds import LatestNewsFeed


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:title_slug>/', views.product_view, name='product'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('news/', views.news, name='news'),
    path('news/<str:title_slug>/', views.news_item, name='news_item'),
    path('rss/news/', LatestNewsFeed(), name='news_feed'),
]
