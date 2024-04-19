# user/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username, is_staff=False)  # Assuming user accounts are not staff
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

# user/views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and not user.is_staff:  # Assuming user accounts are not staff
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
