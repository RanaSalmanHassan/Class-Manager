from django.urls import path
from . import views
app_name = 'loginapp'


urlpatterns = [
    path('SignUp',views.SignUp,name='SignUp'),   
    path('Login',views.Login,name='Login'),
    path('teacher_profile', views.teacher_profile, name='teacher_profile'),
    path('student_profile', views.student_profile, name='student_profile'),
]