from . import views
from django.urls import path
app_name = 'teacher_app'

urlpatterns = [
	path('', views.teacher_home, name='teacher_home'),
	path('message_to_student', views.message_to_student, name='message_to_student'),
	path('messages_all', views.messages_all, name='messages_all'),
]
