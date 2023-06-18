from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User




class Diary(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(User, related_name='user_diary',null=False,on_delete=models.CASCADE)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    # diary = models.ForeignKey(Diary,null=True, on_delete=models.CASCADE)
    diary = models.IntegerField()
    
class Question(models.Model):
    title = models.CharField(max_length=80)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, related_name='user_answer', on_delete=models.CASCADE)
    content = models.TextField()
    content = models.TextField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    
    
    

# Create your models here.
