from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_view),
    path('signup/',views.signUp_view)
    
]
