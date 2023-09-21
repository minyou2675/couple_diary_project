from django.shortcuts import render
from rest_framework import generics
from .serializers import DiarySerializer
from diary.models import Diary

# Create your views here.

class DiaryView(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    