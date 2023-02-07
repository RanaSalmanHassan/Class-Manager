from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, Teacher_Profile_Form, Student_Profile_Form,Edit_Student_Form,Edit_Teacher_Form
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import StudentProfile,TeacherProfile
# Create your views here.


# def SignUp(request):
#     form = SignUpForm()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 if user.is_teacher:
#                     login(request, user)
#                     return HttpResponse('<h1>TEACHER HAS SIGNED UP</h1>')
#                 elif user.is_student:
#                     login(request, user)
#                     return HttpResponse('<h1> Student Have Signed Up</h1>')
#                 else:
#                     return HttpResponse('Sorry Wrong Credential!')
#     dict = {'form': form}
#     return render(request, 'loginapp/signup.html', dict)

def Teacher_Sign_Up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        profile = Teacher_Profile_Form(data=request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            userform.is_teacher = True
            userform.save()

            profileboi = profile.save(commit=False)
            profileboi.teacher = userform
            profileboi.save()

            # return HttpResponse('Signed Up')
            return HttpResponseRedirect(reverse('loginapp:Login'))
        else:
            messages.warning(request,f' There is error in your form : {form.errors} {profile.errors}')

    else:
        form = SignUpForm()
        profile = Teacher_Profile_Form()

    dict = {'form': form, 'profile': profile}
    return render(request, 'loginapp/teacher_signup.html', dict)


def Student_Sign_Up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile = Student_Profile_Form(request.POST)
        if form.is_valid() and profile.is_valid():
            userform = form.save(commit=False)
            userform.is_student = True
            userform.save()

            profileboi = profile.save(commit=False)
            profileboi.student = userform
            profileboi.save()

            # return HttpResponse('Signed Up')
            return HttpResponseRedirect(reverse('loginapp:Login'))

        else:
            messages.warning(
                request, f' There is error in your form : {form.errors} {profile.errors}')
    else:
        form = SignUpForm()
        profile = Student_Profile_Form()

    dict = {'form': form, 'profile': profile}
    return render(request, 'loginapp/student_signup.html', dict)


def SignUp(request):
    return render(request, 'loginapp/signup.html')


def Login(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                # return HttpResponseRedirect(reverse('loginapp:edit_profile'))
                if user.is_teacher:
                    return HttpResponseRedirect(reverse('teacher_app:teacher_home'))

                elif user.is_student:
                    return HttpResponseRedirect(reverse('student_app:student_home'))
                else:
                    return HttpResponse('You are not welcomed here!')
        else:
            messages.warning(
                request, f' There is error in your form : {form.errors} ')

    dict = {'form': form}
    return render(request, 'loginapp/login.html', dict)


@login_required(login_url='loginapp:Login')
def edit_profile(request):
    current_user = request.user
    if current_user.is_student:
        student = StudentProfile.objects.get(student=current_user)
        form = Edit_Student_Form(instance=student)
        if request.method == 'POST':
            form = Edit_Student_Form(request.POST,request.FILES,instance=student)
            if form.is_valid():
                form.save()
                form = Edit_Student_Form(instance=student)
                # return HttpResponse('Edited')
                return HttpResponseRedirect(reverse('loginapp:profile'))
        dict = {'form': form}
        return render(request, 'loginapp/edit_profile.html', dict)
    elif current_user.is_teacher:
        student = TeacherProfile.objects.get(teacher=current_user)
        form = Edit_Teacher_Form(instance=student)
        if request.method == 'POST':
            form = Edit_Teacher_Form(
                request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                form = Edit_Teacher_Form(instance=student)
                # return HttpResponse('Edited')
                return HttpResponseRedirect(reverse('loginapp:profile'))
        dict = {'form':form}
        return render(request,'loginapp/edit_profile.html',dict)

@login_required(login_url='loginapp:Login')
def profile(request):
    current_user = request.user
    if current_user.is_teacher:
        Teacher = TeacherProfile.objects.get(teacher=current_user)
        dict = {'Teacher':Teacher}
        return render(request,'loginapp/teacher_profile.html',dict)
    elif current_user.is_student:
        Student = StudentProfile.objects.get(student=current_user)
        dict = {'Student':Student}
        return render(request,'loginapp/student_profile.html',dict)

    else:
        return HttpResponse('Sorry You Don`t Have an Account!')

@login_required(login_url='loginapp:Login')
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginapp:Login'))


# @login_required(login_url='loginapp:Login')
# def user_profile(request):
#     current_user = request.user
#     if current_user.is_student:
#         Student = StudentProfile.objects.get(student=request.user)
#         dict = {'Student': Student}
#         return render(request, 'loginapp/student_profile.html', dict)
#     elif current_user.is_teacher:
#         Teacher = TeacherProfile.objects.get(student=request.user)
#         dict = {'Teacher': Teacher}
#         return render(request, 'loginapp/teacher_profile.html',dict)
#     else:
#         return HttpResponse('Sorry You haven`t logged in')
# @login_required(login_url='loginapp:Login')
# def make_profile(request):
#     current_user = request.user
#     if current_user.is_teacher:
#         form = Edit_Teacher_Profile_Form()
#         if request.method == 'POST':
#             form = Edit_Teacher_Profile_Form(request.POST,request.FILES)
#             if form.is_valid():
#                 teacherboi = form.save(commit=False)
#                 teacherboi.teacher = request.user
#                 teacherboi.save()
#                 messages.success(request, 'Teacher Profile Updated!')
#                 return HttpResponseRedirect(reverse('loginapp:user_profile'))
#         dict = {'form': form}
#         return render(request, 'loginapp/edit_teacher_profile.html', dict)
#     elif current_user.is_student:
#         form = Edit_Student_Profile_Form()
#         if request.method == 'POST':
#             form = Edit_Student_Profile_Form(request.POST,request.FILES)
#             if form.is_valid():
#                 studentboi = form.save(commit=False)
#                 studentboi.student = request.user
#                 studentboi.save()
#                 messages.success(request, 'Student Profile Updated!')
#                 return HttpResponseRedirect(reverse('loginapp:user_profile'))
#         dict = {'form': form}
#         return render(request, 'loginapp/edit_student_profile.html', dict)

#     else:
#         return HttpResponse("<h1> Sorry You can`t change profile!</h1>")
