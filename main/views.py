from django.shortcuts import render
from .models import Product

def show_info(request):
    context = {
        'app_name': 'Toko Sepatu Sejahtera',
        'name': 'Bisma Zharfan Satryo Wibowo',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
