from django.contrib import admin
from .models import Question,Diary,Answer,Schedule

# Register your models here.
admin.site.register(Question)
admin.site.register(Diary)
admin.site.register(Answer)
admin.site.register(Schedule)