import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from urllib3 import request
from .models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
        
    context = {
        'npm': '2406355136',
        'name': request.user.username,
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return JsonResponse({
                "success": True,
                "message": "Your account has been successfully created!",
                "redirect_url": "/login/"  # ganti sesuai url login kamu
            })
        else:
            # kirim error dalam bentuk dictionary
            messages.error(request, "Account creation failed. Please correct the errors below.")
            return JsonResponse({
                "success": False,
                "errors": form.errors,
            }, status=400)
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'redirect_url': reverse('main:show_main')
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'non_field_errors': form.non_field_errors()
            })
    
    # kalau GET, tetap render normal untuk form login
    else:
        form = AuthenticationForm(request)
        return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    response = JsonResponse({
        'success': True, 
        'redirect_url': reverse('main:login')
    })
    response.delete_cookie('last_login')
    return response

def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()

            # Kalau request AJAX, kirim JSON
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': "Product created successfully!"
                })

            messages.success(request, "Product created successfully!")
            return redirect('main:show_main')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)
            messages.error(request, "Failed to create product.")

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                messages.success(request, "Product updated successfully!")
                return JsonResponse({'success': True, 'message': 'Product updated successfully!'})
            return redirect('main:show_product', id=product.id)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ProductForm(instance=product)
    context = {'form': form
               , 'product': product}

    return render(request, "edit_product.html", context)

@csrf_exempt
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated = form.save()
            return JsonResponse({
                "id": str(updated.id),
                "name": updated.name,
                "brand": updated.brand,
                "price": updated.price,
                "rating": updated.rating,
                "category": updated.category,
                "thumbnail": updated.thumbnail,
                "description": updated.description,
                "is_featured": updated.is_featured,
            })
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    brand = strip_tags(request.POST.get("brand"))
    price = strip_tags(request.POST.get("price"))
    rating = strip_tags(request.POST.get("rating"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name,
        brand=brand,
        price=price,
        rating=rating,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)   

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'brand': product.brand,
            'price': product.price,
            'rating': product.rating,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
                'id': str(product.id),
                'name': product.name,
                'brand': product.brand,
                'price': product.price,
                'rating': product.rating,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'created_at': product.created_at.isoformat() if product.created_at else None,
                'is_featured': product.is_featured,
                'user_id': product.user_id,
                'user_username': product.user.username if product.user_id else None,
            }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

