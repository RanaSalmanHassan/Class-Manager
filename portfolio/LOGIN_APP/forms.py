from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,TeacherProfile,StudentProfile
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2','captcha')

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()


class Teacher_Profile_Form(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('teacher',)


class Student_Profile_Form(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('student',)

class Edit_Teacher_Form(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('teacher',)


class Edit_Student_Form(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('student',)
