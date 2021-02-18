from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('products/', views.products, name='accounts-products'),
    path('customer/<str:pk>', views.customer, name='accounts-customer'),
]
