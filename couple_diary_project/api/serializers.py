from rest_framework import serializers
from diary.models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id','title','content','image',
                  'author','day','month','year','created_at')
        