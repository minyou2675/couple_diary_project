from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from datetime import datetime
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request,'diary/index.html')


def showDiaryCreate(request):
    if request.method == 'GET':
        return render(request, 'diary/diarycreate.html',{})
    elif request.method == 'POST':
        author = request.user
        image = request.FILES['chooseFile']
        title = request.POST['diaryTitle']
        content = request.POST['diaryContent']
        month = datetime.today().month
        year = datetime.today().year
        day = datetime.today().day
        newDiary = Diary(image=image,title=title,content=content,year=year,month=month,day=day,author=author)
        newDiary.save()
        return redirect('/dailydiary/')

def showDailyDiary(request):
    mintUser = User.objects.get(pk=1)
    lemonUser = User.objects.get(pk=2)
    month = datetime.today().month
    year = datetime.today().year
    day = datetime.today().day
    mintDiary = Diary.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonDiary = Diary.objects.filter(author=lemonUser,year=year,month=month,day=day)
    context = {'mintDiary' : mintDiary, 'lemonDiary' : lemonDiary}
    return render(request, 'diary/dailydiary.html',context)

def showCalandar(request):
    return render(request,'diary/calandar.html',{})

def showQuestion(request):
    mintUser = User.objects.get(pk=1)
    lemonUser = User.objects.get(pk=2)
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    
    print("year month day",year,month,day)
    
    mintAnswer = Question.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonAnswer = Question.objects.filter(author=lemonUser,year=year,month=month,day=day)
    
    context = {'mintAnswer' : mintAnswer, 'lemonAnswer' : lemonAnswer} 
    
    return render(request,'diary/todayquestion.html',context)

def saveAnswer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        userkey = request.POST.get('user')
        user = User.objects.get(pk=userkey)
        day = request.POST.get('day')
        year = request.POST.get('year')
        month = request.POST.get('month')
        newQuestion = Question(title=title,content=content,year=year,month=month,day=day,author=user)
        newQuestion.save()
        data = {'title':title, 'content':content,'userkey':userkey,'day':day,'month':month,'year':year}
        print(data)
        return redirect('/calandar/')
    else:
        return render(request, 'diary/todayquestion.html',{})
    
    