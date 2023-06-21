from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # email = models.EmailField(unique=True,default='')
    # USERNAME_FIELD = 'email'
    partner = models.EmailField(null=True,blank=True,unique=True,verbose_name=_("연인의 이메일 주소"))
    COLOR_CHOICES = (('mint',"Mint"),('lemon','Lemon'))
    color = models.CharField(max_length=10,null=False,choices=COLOR_CHOICES)

    