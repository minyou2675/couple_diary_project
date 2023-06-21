from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django.contrib.auth import authenticate 
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("유효하지 않은 아이디 또는 비밀번호 입니다.")

class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','partner','color','password']
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '나의 Email'}))
    # partner = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '상대방의 Email'}))
    # color = forms.ChoiceField(choices=(('mint','Mint'),('lemon','Lemon')),widget=forms.ChoiceWidget(attrs={'placeholder': 'color'}))
    # first = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '처음 사귄 날'}))
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email
    
    def clean_color(self):
        color = self.cleaned_data['color']
        return color
    
    def clean_partner(self):
        partner = self.cleaned_data['partner']
        if User.objects.filter(partner=partner).exists():
            raise forms.ValidationError('Partner already exists.')
        return partner

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError('Passwords do not match.')

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        color = self.cleaned_data['color']
        partner = self.cleaned_data['partner']
  
        user = User.objects.create_user(username=username, email=email, password=password,color=color,partner=partner)
        return user