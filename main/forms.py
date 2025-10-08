from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "rating", "description", "thumbnail", "category", "is_featured"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        return strip_tags(rating)

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data["thumbnail"]
        return strip_tags(thumbnail)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)