from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User




class Diary(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Question(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

# Create your models here.
