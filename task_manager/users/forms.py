from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Users


class UsersForm(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'username',
        ]