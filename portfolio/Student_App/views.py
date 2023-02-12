from django.shortcuts import render, HttpResponseRedirect
from LOGIN_APP.models import Message,TeacherProfile
from LOGIN_APP.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from Teacher_App.models import Assignment


# Create your views here.


@login_required(login_url='loginapp:Login')
def student_home(request):
    return render(request, 'student_app/home.html')


@login_required(login_url='loginapp:Login')
def message_to_teacher(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            formboi = form.save(commit=False)
            formboi.user_sender = request.user
            formboi.save()
            messages.success(request, 'Your Message is Sent Successfully!!')
            return HttpResponseRedirect(reverse('loginapp:profile'))

    dict = {'form': form}
    return render(request, 'student_app/messages_to.html', dict)


@login_required(login_url='loginapp:Login')
def inbox(request):
    sent_messages = Message.objects.filter(user_sender=request.user)
    recieved_messages = Message.objects.filter(user_reciever=request.user)
    dict = {'sent_messages': sent_messages,
            'recieved_messages': recieved_messages}
    return render(request, 'student_app/inbox.html', dict)


@login_required(login_url='loginapp:Login')
def student_options(request):
    return render(request, 'student_app/student_options.html')

@login_required(login_url='loginapp:Login')
def all_assignments(request):
    all_assignments_for_students = Assignment.objects.all()
    dict = {'all_assignments_for_students':all_assignments_for_students}
    return render(request,'student_app/all_assignments.html',dict)

@login_required(login_url='loginapp:Login')
def all_teachers(request):
    all_teachers_of_school = TeacherProfile.objects.all()
    dict = {'all_teachers_of_school':all_teachers_of_school}
    return render(request,'student_app/all_teachers.html',dict)
