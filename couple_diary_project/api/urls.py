from django.urls import path
from . import views
from .views import DiaryView,ShowDiaryView

urlpatterns = [
    path('diary',DiaryView.as_view()),
    path('showdiary',ShowDiaryView.as_view())
       
]
