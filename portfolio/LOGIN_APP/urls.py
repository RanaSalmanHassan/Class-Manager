from django.urls import path
from . import views
app_name = 'loginapp'


urlpatterns = [
    path('Teacher_Sign_Up', views.Teacher_Sign_Up, name='Teacher_Sign_Up'),
    path('Student_Sign_Up', views.Student_Sign_Up, name='Student_Sign_Up'),
    path('Login',views.Login,name='Login'),
    path('Logout', views.Logout, name='Logout'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('profile', views.profile, name='profile'),
    # path('user_profile', views.user_profile, name='user_profile'),
    # path('make_profile', views.make_profile, name='make_profile'),
]