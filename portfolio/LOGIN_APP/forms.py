from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from captcha.fields import CaptchaField

class SignUpForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2','is_teacher','is_student','captcha')

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()