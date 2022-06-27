from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)