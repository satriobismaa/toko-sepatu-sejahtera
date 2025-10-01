import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('sneakers', 'Sneakers'),
        ('boots', 'Boots'),
        ('sandals', 'Sandals'),
        ('formal', 'Formal Shoes'),
        ('sports', 'Sports Shoes'),
        ('casual', 'Casual Shoes'),
        ('loafers', 'Loafers'),
        ('heels', 'Heels'),
        ('flats', 'Flats'),
        ('slippers', 'Slippers'),
        ('other', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #id produk
    name = models.CharField(max_length=100) #nama dari produk   
    brand = models.CharField(max_length=50) #merek produk
    price = models.IntegerField() #harga produk
    rating = models.FloatField() #rating produk
    description = models.TextField() #deskripsi produk
    thumbnail = models.URLField() #gambar produk
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update') #kategori produk
    is_featured = models.BooleanField(default=False) #apakah produk merupakan unggulan
    created_at = models.DateTimeField(auto_now_add=True) #tanggal penambahan

    def __str__(self):
        return self.name
    