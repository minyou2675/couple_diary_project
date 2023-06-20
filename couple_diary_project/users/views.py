from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import SignUpForm,LoginForm
from .models import User
 

# Create your views here.
def signUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 완료 후 로그인 처리 등 추가 작업 수행
            return redirect('/user/login/')  # 회원가입 후 리다이렉트할 URL
    
    else:
     form = SignUpForm()   
     return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = request.POST['username'] 
            password = request.POST['password']
            print(username)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                #파트너가 가입이 안되어 있으면 거절
                partner = User.objects.filter(email=user.email)
                if partner is None:
                    error_message = "파트너 계정이 아직 생성되지 않아 로그인이 불가합니다."
                    return render(request,'registration/login.html',{'error_message' : error_message})
                #세션에 user 객체 저장
                login(request, user)
                return redirect('/dailyquestion')  # 로그인 후 리다이렉트할 URL
            else:
                error_message = "유효하지 않은 아이디 또는 비밀번호 입니다."
                return render(request, 'registration/login.html', {'error_message': error_message})
        else:
        
            return render(request, 'registration/login.html',{'form':form})
        
    else:
        form = LoginForm()
        return render(request, 'registration/login.html',{'form':form})