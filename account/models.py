from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class LowercaseEmailField(models.EmailField):
    # Override EmailField to convert emails to lowercase before saving.
    def to_python(self, value):
        value = super(LowercaseEmailField, self).to_python(value)

        if isinstance(value, str):
            return value.lower()
        return value

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=255, blank=False)
    email = LowercaseEmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.full_name or self.email