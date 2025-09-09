from django.urls import path
from main.views import show_info

app_name = 'main'

urlpatterns = [
    path('', show_info, name='show_info'),
]