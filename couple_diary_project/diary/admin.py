from django.contrib import admin
from .models import Question,Diary

# Register your models here.
admin.site.register(Question)
admin.site.register(Diary)