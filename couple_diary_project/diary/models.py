from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib.auth.models import User




class Diary(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='diary/images/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_diary',null=False,on_delete=models.CASCADE)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return f'/diaryupdate/{self.pk}'
    def __str__(self):
        return f'{self.pk}-{self.title}'
    

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
    
    def __str__(self):
        return f'{self.pk}-{self.title}'


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='user_answer', on_delete=models.CASCADE)
    content = models.TextField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.pk}-{self.author}-{self.content}'
    

# Create your models here.
