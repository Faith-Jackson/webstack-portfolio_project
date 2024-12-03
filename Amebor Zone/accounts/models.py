from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
