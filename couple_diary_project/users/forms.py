from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class SignUpForm(forms.ModelForm):
    # username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'SignUpForm'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'signUpForm'}))
    # partner = forms.EmailField(widget=forms.EmailInput(attrs={'class':'signUpForm'}))
    # color = forms.ChoiceField(widget=forms.Select(choices=(('mint','Mint'),('lemon','Lemon')),attrs={'class':'colorSelect'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'signUpForm'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'signUpForm'}))

    class Meta:
        model = User
        fields = ['username','email','partner','color','password']
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
        user = User.objects.create_user(username=username, email=email, password=password)
        return user