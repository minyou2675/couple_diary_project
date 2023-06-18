from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dailyquestion/', views.showQuestion),
    path('saveanswer/',views.saveAnswer),
    path('calandar/', views.showCalandar),
    path('dailydiary/',views.showDailyDiary),
    path('diarycreate/<int:pk>/',views.showDiaryCreate),
    path('questionlist/',views.showQuestionList),
    path('diary/<int:pk>',views.showDiary),
    
    
]
