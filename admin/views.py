# admin/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class AdminAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username, is_staff=True)  # Assuming admin users are staff
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

# admin/views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


# admin/views.py
from rest_framework import viewsets
from .models import Bus
from .serializers import BusSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    @action(detail=True, methods=['post'], url_path='upload-seat-status')
    def upload_seat_status(self, request, pk=None):
        bus = self.get_object()
        seat_status = request.data.get('seat_status', {})
        bus.seat_status = seat_status
        bus.save()
        serializer = self.get_serializer(bus)
        return Response(serializer.data)

