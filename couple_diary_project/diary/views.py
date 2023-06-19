from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from datetime import datetime
from django.http import JsonResponse
from calendar import monthcalendar,monthrange 
import random


# Create your views here.

def index(request):
    return render(request,'diary/index.html')

def showDiary(request,pk):
    date = str(pk)
    date = datetime.strptime(date,'%Y%m%d')
    print(date)
    year = date.year
    month = date.month
    day = date.day
    print(day,month,year)
    mintUser = User.objects.get(pk=1)
    lemonUser = User.objects.get(pk=2)
    mintDiary = Diary.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonDiary = Diary.objects.filter(author=lemonUser,year=year,month=month,day=day)

    return render(request,'diary/diary.html',context={'mintDiary' : mintDiary, 'lemonDiary':lemonDiary})

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


    
    

def showDiaryCreate(request,pk):
    if request.method == 'GET':
        month = datetime.today().month
        year = datetime.today().year
        day = datetime.today().day
        if pk == 1:
            user = 'mint'
        else:
            user = 'lemon'
        schedule = Schedule.objects.filter(year=year,month=month,day=day)
        if schedule:
            pass
        else:
            schedule = Schedule(year=year,month=month,day=day,diary=0)
            schedule.save()
            
        return render(request, 'diary/diarycreate.html',{'user' : user})
    elif request.method == 'POST':
        # author = request.user
        author = User.objects.get(pk=pk)
        if request.FILES.get('chooseFile') is not None:
            image = request.FILES.get('chooseFile')
        else:
            image = None
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

def moveCalendar(request,pk):
    monthList = {1 : 'JAN', 2 : 'FEB', 3 : 'MAR', 4 : 'APR', 5 : 'MAY', 6 : 'JUN', 7 : 'JUL',
                            8 : 'AUG', 9: 'SEP', 10 : 'OCT', 11: 'NOV', 12 : 'DEC'}
    date = str(pk)
    date = datetime.strptime(date,"%Y%m")
    year = date.year
    month = date.month   
    calendar = monthcalendar(year,month) 
    month_calendar = []
    month_name = monthList[month]
    for week in calendar:   
        week_diary = []
        for day in week:
            if day == 0:
                 week_diary.append({'day' : ' ' , 'diary' : 0})
            else:
                schedule = Schedule.objects.filter(year=year,month=month,day=day)
                if schedule:
                    diary_count = schedule.first().diary
                    week_diary.append({'day' : day  ,'diary' : diary_count})
                else:
                    week_diary.append({'day' : day , 'diary' : 0})
        month_calendar.append({'week':week_diary,'year' : year,'month':month})
    print(month_calendar)
                         
        
    return render(request,'diary/movecalendar.html',{'calendar':month_calendar,'year':year,'month':month,'month_name':month_name})

    print(date)

def showCalendar(request):
    year = datetime.today().year
    month = datetime.today().month
    calendar = monthcalendar(year,month)
    month_calendar = []
    for week in calendar:   
        week_diary = []
        for day in week:
            if day == 0:
                 week_diary.append({'day' : ' ' , 'diary' : 0})
            else:
                schedule = Schedule.objects.filter(year=year,month=month,day=day)
                if schedule:
                    diary_count = schedule.first().diary
                    week_diary.append({'day' : day  ,'diary' : diary_count})
                else:
                    week_diary.append({'day' : day , 'diary' : 0})
        month_calendar.append({'week':week_diary,'year' : year,'month':month})
    print(month_calendar)
                         
        
    return render(request,'diary/calendar.html',{'calendar':month_calendar,'year':year,'month':month})

def showQuestion(request):
    mintUser = User.objects.get(pk=1)
    lemonUser = User.objects.get(pk=2)
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    
    #question title 리스트
    question_title = ['좋아하는 색깔은?','먹고싶은 음식은?','하고싶은 것']
    random_title = random.randint(0,len(question_title))
    question = Question.objects.filter(year=year,month=month,day=day)
    #question 객체 생성
    if(question):
        question_title = question.first().title
    else:
        newQuestion = Question(title=question_title[random_title],year=year,month=month,day=day)
        question_title = question_title[random_title]
        newQuestion.save()
        
    print("year month day",year,month,day)
    
    mintAnswer = Answer.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonAnswer = Answer.objects.filter(author=lemonUser,year=year,month=month,day=day)
    
    context = {'mintAnswer' : mintAnswer, 'lemonAnswer' : lemonAnswer, 'questionTitle' : question_title} 
    
    return render(request,'diary/todayquestion.html',context)

def saveAnswer(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.POST.get('userpk')
        user = User.objects.get(pk=user)
        day = request.POST.get('day')
        year = request.POST.get('year')
        month = request.POST.get('month')
        question = Question.objects.get(year=year,month=month,day=day)
        #최초 답변이면 질문 저장
        newAnswer = Answer(question=question,content=content,author=user,year=year,month=month,day=day)
        newAnswer.save()
        data = {'title':title, 'content':content,'day':day,'month':month,'year':year}
        print(data)
        return redirect('/calandar/')
    else:
        return render(request, 'diary/todayquestion.html',{})
    
    