from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def SignUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_teacher:
                    login(request, user)
                    return HttpResponse('<h1>TEACHER HAS SIGNED UP</h1>')
                elif user.is_student:
                    login(request, user)
                    return HttpResponse('<h1> Student Have Signed Up</h1>')
                else:
                    return HttpResponse('Sorry Wrong Credential!')
    dict = {'form': form}
    return render(request, 'loginapp/signup.html', dict)


def Login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request,user)
                return HttpResponse('LOGGED IN YOU USER BOI!!!!')

    dict = {'form':form}
    return render(request,'loginapp/login.html',dict)


@login_required(login_url='loginapp:Login')
def teacher_profile(request):
    current_user = request.user
    if current_user.is_teacher:
        return render(request,'loginapp/teacher_profile.html')
    else:
        return render(request,'loginapp/student_profile.html')


@login_required(login_url='loginapp:Login')
def student_profile(request):
    current_user = request.user
    if current_user.is_student:
        return render(request,'loginapp/student_profile.html')

    else:
        return render(request,'loginapp/teacher_profile.html')

