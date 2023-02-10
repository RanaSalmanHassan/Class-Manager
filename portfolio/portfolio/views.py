from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return HttpResponseRedirect(reverse('loginapp:profile'))
        elif request.user.is_student:
            return HttpResponseRedirect(reverse('loginapp:profile'))
        else:
            return HttpResponseRedirect(reverse('loginapp:Login'))
    else:
        return HttpResponseRedirect(reverse('loginapp:SignUp'))
