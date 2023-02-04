from django.urls import path
app_name = 'student_app'
from . import views

urlpatterns = [
	path('',views.student_home,name='student_home'),
	path('message_to_teacher',views.message_to_teacher,name='message_to_teacher'),
	path('messages_all',views.messages_all,name='messages_all'),
]
