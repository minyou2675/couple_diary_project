from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dailyquestion/', views.showQuestion),
    path('saveanswer/',views.saveAnswer),
    path('calendar/', views.showCalendar),
    path('calendar/<int:pk>/',views.moveCalendar),
    path('dailydiary/',views.showDailyDiary),
    path('diarycreate/<int:pk>/',views.showDiaryCreate),
    path('questionlist/',views.showQuestionList),
    path('diary/<int:pk>',views.showDiary),
    
    
]
