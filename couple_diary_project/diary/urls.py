from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dailyquestion/', views.showQuestion),
    path('saveanswer/',views.saveAnswer),
    
    
]
