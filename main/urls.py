from django.urls import path
from main.views import show_products

app_name = 'main'

urlpatterns = [
    path('', show_products, name='show_products'),
]