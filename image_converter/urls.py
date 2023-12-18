from django.urls import path
from .views import CompareTexts,ConvertImage2Text

urlpatterns = [
    path('ConvertImage2Text', ConvertImage2Text, name='ConvertImage2Text'),
    path('CompareTexts', CompareTexts, name='CompareTexts'),
]
