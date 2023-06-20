from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import SignUpForm,LoginForm
 

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
            username = form['username']
            password = form['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/diary/todayquestion/')  # 로그인 후 리다이렉트할 URL
            else:
                error_message = "유효하지 않은 아이디 또는 비밀번호 입니다."
                return render(request, 'registration/login.html', {'error_message': error_message})
        else:
            return render(request, 'registration/login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request, 'registration/login.html',{'form':form})