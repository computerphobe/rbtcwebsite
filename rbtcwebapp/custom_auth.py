# custom_auth.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Custom authentication backend that allows case-insensitive usernames.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        # Make the username case-insensitive
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return None

        # Check the password
        if user.check_password(password):
            return user
        return None
