#This is a django urls page 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'), # Access via base URL
    path('colcom-ai/', views.colcom_ai, name='colcom_ai'),
]
