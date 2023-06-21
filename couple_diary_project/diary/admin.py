from django.contrib import admin
from .models import Question,Diary,Answer,Schedule
from users.models import User

# Register your models here.
admin.site.register(Question)
admin.site.register(Diary)
admin.site.register(Answer)
admin.site.register(Schedule)
admin.site.register(User)