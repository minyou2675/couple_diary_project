from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dailyquestion/', views.showQuestion),
    path('saveanswer/',views.saveAnswer),
    path('calendar/<int:pk>/',views.showCalendar),
    path('dailydiary/',views.showDailyDiary),
    path('diarycreate/<int:pk>/',views.showDiaryCreate),
    path('questionlist/<int:pk>',views.showQuestionList),
    path('diary/<int:pk>',views.showDiary),
    path('diaryupdate/<int:pk>',views.diaryUpdate),
    
    
]
