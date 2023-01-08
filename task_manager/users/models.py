from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Users(AbstractUser):

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
