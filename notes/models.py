from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('category-notes', kwargs={'pk': self.pk})

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=False,null=False,default=None)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.category}'

    def get_absolute_url(self):
        return reverse('category-notes',kwargs={'pk':self.category.pk})