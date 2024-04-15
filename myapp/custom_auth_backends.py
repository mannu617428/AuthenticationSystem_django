# In custom_auth_backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class OTPAuthenticationBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, otp=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_otp(otp):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
