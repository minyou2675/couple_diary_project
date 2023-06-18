from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from datetime import datetime
from django.http import JsonResponse
import random


# Create your views here.

def index(request):
    return render(request,'diary/index.html')

def showQuestionList(request):
    month = datetime.today().month
    year = datetime.today().year
    day = datetime.today().day
    mintUser= User.objects.get(pk=1)
    lemonUser= User.objects.get(pk=2)
    mintAnswer = Answer.objects.filter(author=mintUser,month=month,year=year,day=day)
    question = Question.objects.get(year=year,month=month,day=day)

   
    lemonAnswer = Answer.objects.filter(author=lemonUser,month=month,year=year,day=day)
    if lemonAnswer:
        pass
    else:
        lemonAnswer = lemonAnswer.first()
  
    context = {
               'mintAnswer' : mintAnswer,
               'lemonAnswer' : lemonAnswer,
               'question'   : question}
    
    return render(request,'diary/questionlist.html',context)
    
    

def showDiaryCreate(request):
    if request.method == 'GET':
        month = datetime.today().month
        year = datetime.today().year
        day = datetime.today().day
        schedule = Schedule.objects.filter(year=year,month=month,day=day)
        if schedule:
            pass
        else:
            schedule = Schedule(year=year,month=month,day=day,diary=0)
            schedule.save()
        return render(request, 'diary/diarycreate.html',{})
    elif request.method == 'POST':
        author = request.user
        image = request.FILES['chooseFile']
        title = request.POST['diaryTitle']
        content = request.POST['diaryContent']
        month = datetime.today().month
        year = datetime.today().year
        day = datetime.today().day
        
        schedule = Schedule.objects.get(year=year,month=month,day=day)
        newDiary = Diary(image=image,title=title,content=content,year=year,month=month,day=day,author=author)
        schedule.diary +=  1
        schedule.save()
        newDiary.save()
    
        return redirect('/dailydiary/')

def showDailyDiary(request):
    month = datetime.today().month
    year = datetime.today().year
    day = datetime.today().day

    mintUser = User.objects.get(pk=1)
    lemonUser = User.objects.get(pk=2)

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
    
    #question title 리스트
    question_title = ['좋아하는 색깔은?','먹고싶은 음식은?','하고싶은 것']
    random_title = 0
    question = Question.objects.get(year=year,month=month,day=day)
    #question 객체 생성
    if(question):
        question_title = question.title
    else:
        newQuestion = Question(title=question_title[random_title],year=year,month=month,day=day)
        newQuestion.save()
        
    print("year month day",year,month,day)
    
    mintAnswer = Answer.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonAnswer = Answer.objects.filter(author=lemonUser,year=year,month=month,day=day)
    
    context = {'mintAnswer' : mintAnswer, 'lemonAnswer' : lemonAnswer, 'questionTitle' : question_title[random_title]} 
    
    return render(request,'diary/todayquestion.html',context)

def saveAnswer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        day = request.POST.get('day')
        year = request.POST.get('year')
        month = request.POST.get('month')
        question = Question.objects.get(year=year,month=month,day=day)
        #최초 답변이면 질문 저장
        newAnswer = Answer(question=question,author=user,year=year,month=month,day=day)
        newAnswer.save()
        data = {'title':title, 'content':content,'day':day,'month':month,'year':year}
        print(data)
        return redirect('/calandar/')
    else:
        return render(request, 'diary/todayquestion.html',{})
    
    