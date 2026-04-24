#This is a django urls page 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'), # Access via base URL
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('colcom-ai/', views.colcom_ai, name='colcom_ai'),
    path('logout/', views.logout_view, name='logout'),
]
