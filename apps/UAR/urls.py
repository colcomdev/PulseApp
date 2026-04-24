from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_request, name='create_request'),
    path('approve/<int:id>/', views.approve, name='approve'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('security_log/', views.security_entry, name='security_entry'),
    path('success/', views.success, name='success'),
    path('logs/', views.security_logs, name='security_logs'),
]
"""urlpatterns = [
    path('', views.RequestRights, name='requests'), # Access via base URL
    path('request_list/', views.ApproveRights, name='request_list'), # Access via base URL
    path('request_details/', views.RequestDetails, name='request_details'), # Access via base URL
]
"""