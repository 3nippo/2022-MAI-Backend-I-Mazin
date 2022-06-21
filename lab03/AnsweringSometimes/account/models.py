from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from rest_framework import serializers

def validate_age(age):
    if age <= 0:
        raise ValidationError(
            _('age=%(age)i is not possible'),
            params={'age': age},
        )

# Create your models here.
class User(AbstractUser):
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
    
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['age', 'gender']

    class Meta:
        db_table = 'users'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'gender']
