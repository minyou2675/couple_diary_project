from django.urls import path
from . import views
from .views import DiaryView

urlpatterns = [
    path('diary',DiaryView.as_view()),
       
]
