from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.user.username

# Create your models here.
