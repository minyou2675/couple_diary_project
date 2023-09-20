from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from .forms import SignUpForm,LoginForm
from .models import User
 

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/user/login')




def signUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user = form.save()
            user.save()
            # 회원가입 완료 후 로그인 처리 등 추가 작업 수행
            return redirect('/user/login/')  # 회원가입 후 리다이렉트할 URL
        else:
            form = SignUpForm()
            return render(request, 'registration/signup.html', {'form': form})
    
    else:
     form = SignUpForm()
     if request.user in User.objects.all():
         return redirect('/todayquestion/')   
     return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid() or request.form.get('test-mode') == 'locust-test':
            username = request.POST['username'] 
            password = request.POST['password']
            print(username)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                #파트너가 가입이 안되어 있으면 거절
                partner = User.objects.filter(email=user.partner)
                if partner.exists():
                     # 로그인 후 리다이렉트할 URL
                    login(request, user)
                    return redirect('/dailyquestion') 
                else:
                    error_message = "파트너 계정이 아직 생성되지 않아 로그인이 불가합니다."
                    form = LoginForm()
                    return render(request,'registration/login.html',{'form':form,'error_message' : error_message})
               
              
                    
            else:
                error_message = "유효하지 않은 아이디 또는 비밀번호 입니다."
                form = LoginForm()
                return render(request, 'registration/login.html', {'form':form,'error_message': error_message})
        else:
        
            return render(request, 'registration/login.html',{'form':form})
        
    else:
        
        if request.user.is_authenticated:
            return redirect('/dailyquestion/')
        else:
            form = LoginForm()
            return render(request, 'registration/login.html',{'form':form})