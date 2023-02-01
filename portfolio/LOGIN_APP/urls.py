from django.urls import path
from . import views
app_name = 'loginapp'


urlpatterns = [
    path('SignUp',views.SignUp,name='SignUp'),   
    path('Login',views.Login,name='Login'),   
]