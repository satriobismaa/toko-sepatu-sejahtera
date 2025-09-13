from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_product, name='create_news'),
    path('news/<str:id>/', show_product, name='show_news'),
    path('products/xml/', show_xml, name='show_xml'),
    path('products/json/', show_json, name='show_json'),
    path('products/xml/<int:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('products/json/<int:product_id>/', show_json_by_id, name='show_json_by_id'),
]