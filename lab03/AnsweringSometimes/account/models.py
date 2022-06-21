from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def validate_age(age):
    if age <= 0:
        raise ValidationError(
            _('age=%(age)i is not possible'),
            params={'age': age},
        )

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, blank=False, unique=True)
    USERNAME_FIELD = 'username'

    email = models.CharField(max_length=30, blank=False, unique=True)

    age = models.SmallIntegerField(
        validators=[validate_age],
        blank=False
    )

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        DIFFERENT = 'D', _('Different')

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        blank=False
    )

    name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    
    REQUIRED_FIELDS = ['name', 'last_name', 'age', 'gender']

    class Meta:
        db_table = 'users'
