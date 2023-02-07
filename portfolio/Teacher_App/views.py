from django.shortcuts import render,HttpResponseRedirect
from LOGIN_APP.models import Message
from LOGIN_APP.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.
@login_required(login_url='loginapp:Login')
def teacher_home(request):
	return render(request,'teacher_app/home.html')

@login_required(login_url='loginapp:Login')
def message_to_student(request):
	form = MessageForm()
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			formboi = form.save(commit=False)
			formboi.user_sender = request.user
			formboi.save()
			messages.success(request,'Your Message is Sent Successfully!!')
			return HttpResponseRedirect(reverse('loginapp:profile'))

	dict = {'form':form}
	return render(request,'teacher_app/messages_to.html',dict)

@login_required(login_url='loginapp:Login')
def messages_all(request):
	sent_messages = Message.objects.filter(user_sender=request.user)
	recieved_messages = Message.objects.filter(user_reciever=request.user)
	dict = {'sent_messages':sent_messages,'recieved_messages':recieved_messages}
	return render(request,'teacher_app/messages_all.html',dict)