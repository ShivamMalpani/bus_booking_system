# admin/urls.py
from django.urls import path
from .views import admin_login, BusViewSet

urlpatterns = [
    path('login/', admin_login, name='admin-login'),
    path("bus/", BusViewSet.as_view(), name='bus-list'),
    path("/buses/<id>/upload-seat-status/", BusViewSet.as_view({'post': 'upload_seat_status'}), name="upload-seat-status"),
    
]
