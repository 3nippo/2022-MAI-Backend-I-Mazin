from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Users(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        DIFFERENT = 'D', _('Different')

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    year_in_school = models.CharField(
        max_length=1,
        choices=Gender.choices
    )

    class Meta:
        db_table = 'users'


class Credentials(models.Model):
    cred_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    login_ref = models.BinaryField()
    password_ref = models.BinaryField()

    class Meta:
        db_table = 'credentials'
