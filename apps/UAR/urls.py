from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestRights, name='requests'), # Access via base URL
    path('request_list/', views.ApproveRights, name='request_list'), # Access via base URL
    path('request_details/', views.RequestDetails, name='request_details'), # Access via base URL
]
