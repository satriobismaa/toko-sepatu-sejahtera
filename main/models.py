import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)             #nama dari produk   
    brand = models.CharField(max_length=50)             #merek produk
    price = models.IntegerField()                       #harga produk
    rating = models.FloatField()                        #rating produk
    description = models.TextField()                    #deskripsi produk
    thumbnail = models.URLField()                       #gambar produk
    category = models.CharField(max_length=50)          #kategori produk
    is_featured = models.BooleanField(default=False)    #apakah produk merupakan unggulan

    def __str__(self):
        return self.name