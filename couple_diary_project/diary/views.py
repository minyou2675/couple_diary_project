from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from users.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from datetime import datetime,timedelta
from django.http import JsonResponse
from calendar import monthcalendar,monthrange 
import random
from django.contrib import messages


# Create your views here.

#기념일 구하는 함수
def celebration(first,delta): #first는 %Y%m%d 형식 delta는 기념일에 해당하는 일수 
    after_delta_days = first + timedelta(days=delta-1)
    return after_delta_days

def index(request):
    return render(request,'diary/index.html')

def diaryUpdate(request,pk):
    user = request.user
    diary = get_object_or_404(Diary,pk=pk)
    # if user != diary.author:
    #         messages.error(request, '수정권한이 없습니다')
    #         return redirect('/dailydiary')
    if request.method == 'POST':  
        title = request.POST['title']
        image = request.FILES.get('chooseFile') if request.FILES.get('chooseFile') is not None else None
        content = request.POST['content']
        diary.title = title
        diary.image = image
        diary.content = content
        diary.save()
        return redirect('diary:dailydiary')
    return render(request,'diary/diaryupdate.html',{'user':user})

def showDiary(request,pk):
    date = str(pk)
    date = datetime.strptime(date,'%Y%m%d')
    print(date)
    year = date.year
    month = date.month
    day = date.day
    print(day,month,year)
    user = request.user
    partner = User.objects.filter(email=user.partner).first()
    if user.color == 'mint':
        mintUser = request.user
        lemonUser = partner
    else:
        lemonUser = request.user
        mintUser = partner
    mintDiary = Diary.objects.filter(author=mintUser,year=year,month=month,day=day)
    lemonDiary = Diary.objects.filter(author=lemonUser,year=year,month=month,day=day)

    if mintDiary:
        mintDiary = mintDiary.last()
    if lemonDiary:
        lemonDiary = lemonDiary.last()


    return render(request,'diary/diary.html',context={'mintDiary' : mintDiary, 'lemonDiary':lemonDiary,'year':year,'month':month,'user':user})

def showQuestionList(request,pk):
    #오늘의 질문 구하기
    month = datetime.today().month
    year = datetime.today().year
    day = datetime.today().day
    today_question = Question.objects.get(year=year,month=month,day=day)
    
    #유저답변 필터링
    user = request.user
    partner = User.objects.filter(email=user.partner).first()
    if user.color == 'mint':
        mintUser = request.user
        lemonUser = partner
    else:
        lemonUser = request.user
        mintUser = partner
    
    all_question_count = Question.objects.all().count()
    print(all_question_count)
    question = Question.objects.all().order_by('-id')[(pk-1)*4:pk*4].values()
    question_list = []
    
    #마지막 페이지 값 연산
    endPage = True if all_question_count <= pk*4  else False

     
    for i in question:
        question_id = i['id']
        q = Question.objects.get(pk=question_id)
        answer_list = {'question' : q ,'mintAnswer' :  '', 'lemonAnswer': ''}
        mintAnswer = Answer.objects.filter(author=mintUser,question=q) 
        lemonAnswer = Answer.objects.filter(author=lemonUser,question=q)
        if mintAnswer:
            answer_list['mintAnswer'] = mintAnswer.first().content
        if lemonAnswer:
            answer_list['lemonAnswer'] = lemonAnswer.first().content
        question_list.append(answer_list)
    print(question_list)
            
             
    context = {'year':year,'month':month,'question_list' : question_list,'pk':pk,'endPage':endPage,'today_question':today_question}
    
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
        author = request.user
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

    # mintUser = User.objects.get(pk=1)
    # lemonUser = User.objects.get(pk=2)
    
    #유저 값 받아오기
    user = request.user
    partner = User.objects.filter(email=user.partner)
    
    if partner:
        partner = partner.first()

    if user.color == 'mint':
        mintUser = user
        lemonUser = partner
    else:
        lemonUser = user
        mintUser = partner
        

    mintDiary = Diary.objects.filter(author=mintUser,year=year,month=month,day=day)
    if mintDiary:
        mintDiary = mintDiary.last()
    lemonDiary = Diary.objects.filter(author=lemonUser,year=year,month=month,day=day)
    if lemonDiary:
        lemonDiary = lemonDiary.last()
      
    context = {'year':year,'month':month,'mintDiary' : mintDiary, 'lemonDiary' : lemonDiary}
    return render(request, 'diary/dailydiary.html',context)

def showCalendar(request,pk):
    #1일
    first = datetime(2023,1,12)
    #100일 기념 
    after_100_days = celebration(first,100)
    
    
    monthList = {1 : 'JAN', 2 : 'FEB', 3 : 'MAR', 4 : 'APR', 5 : 'MAY', 6 : 'JUN', 7 : 'JUL',
                            8 : 'AUG', 9: 'SEP', 10 : 'OCT', 11: 'NOV', 12 : 'DEC'}
    date = str(pk)
    date = datetime.strptime(date,"%Y%m")
    year = date.year
    month = date.month   
    
    #해당 월에 기념일이 있는지
        #100일
    if year == after_100_days.year and month == after_100_days.month:
        day_100 = after_100_days.day 
    else:
        day_100 = 0
        #첫 일
    if year == first.year and month == first.month:
        day_1 = first.day
    else:
        day_1 = 0
    
    
    calendar = monthcalendar(year,month) 
    month_calendar = []
    month_name = monthList[month]
    for week in calendar:   
        week_diary = []
        for day in week:
            if day == 0:
                 week_diary.append({'day' : ' ' , 'diary' : 0})
            else:
                is_day_1 = True if day_1 == day else False
                is_day_100 = True if day_100 == day else False
                schedule = Schedule.objects.filter(year=year,month=month,day=day)
                if schedule:
                    diary_count = schedule.first().diary
                    week_diary.append({'day' : day  ,'diary' : diary_count , 'is_day_1' : is_day_1, 'is_day_100' : is_day_100})
                else:
                    week_diary.append({'day' : day , 'diary' : 0,'is_day_1' : is_day_1, 'is_day_100' : is_day_100})
        month_calendar.append({'week':week_diary,'year' : year,'month':month})
    # print(month_calendar)
    print(day_100,day_1)
                         
        
    return render(request,'diary/calendar.html',{'calendar':month_calendar,'year':year,'month':month,'month_name':month_name})

    
def showQuestion(request):
    user = request.user
    partner = User.objects.filter(email=user.partner)
    
    #파트너 계정이 존재한다면, 단일 객체를 불러옴 
    if partner:
        partner = partner.first()
    if user.color == 'mint':
        mintUser = user
        lemonUser = partner
    else:
        lemonUser = user
        mintUser = partner
    
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
        user = request.user
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
    
    