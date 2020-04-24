from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile/',default='profile/default.jpg', blank=True)
    is_author = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20,db_index=True,blank=True)
    # bio = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile/',default='profile/default.jpg', blank=True)

    def __str__(self):
        return self.user.username
