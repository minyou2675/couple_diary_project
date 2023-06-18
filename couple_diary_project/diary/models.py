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

class Schedule(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
class Question(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.TextField()
    content = models.TextField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    
    
    

# Create your models here.
