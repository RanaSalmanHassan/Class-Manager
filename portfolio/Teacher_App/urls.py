from . import views
from django.urls import path
app_name = 'teacher_app'

urlpatterns = [
	path('', views.teacher_home, name='teacher_home'),
	path('message_to_student', views.message_to_student, name='message_to_student'),
	path('messages_all', views.messages_all, name='messages_all'),
	path('send_assignments', views.send_assignments, name='send_assignments'),
	path('all_assignments', views.all_assignments, name='all_assignments'),
	path('notice_to_students', views.notice_to_students, name='notice_to_students'),
	path('teacher_options', views.teacher_options, name='teacher_options'),
]
