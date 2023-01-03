from django.contrib.auth.forms import UserCreationForm
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
