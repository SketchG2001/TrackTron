from django.contrib.auth.backends import BaseBackend
from .models import Employee

class CustomUserAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Employee.objects.get(username=username)
            if user.check_password(password):
                return user
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None
