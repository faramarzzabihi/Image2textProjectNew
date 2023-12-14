# image_converter/urls.py
from django.urls import path
from .views import convert_image_to_text
from .views import compare_texts,convert_image_to_text

urlpatterns = [
    path('convert_image_to_text', convert_image_to_text, name='convert_image_to_text'),
    path('compare_texts', compare_texts, name='compare_texts'),
]
