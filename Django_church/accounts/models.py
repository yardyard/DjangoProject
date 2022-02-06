from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    university = models.CharField(max_length=50)
    team = models.CharField(max_length=30)
    



#class Profile(models.Model):
   # pass