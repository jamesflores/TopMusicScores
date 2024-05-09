from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:title_slug>/', views.product_view, name='product'),
    path('about/', views.about, name='about'),
]
