from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataMatrix, name='DataMatrix'), # Access via base URL
]
