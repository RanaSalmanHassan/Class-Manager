from . import views
from django.urls import path
app_name = 'student_app'

urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('message_to_teacher', views.message_to_teacher, name='message_to_teacher'),
    path('inbox', views.inbox, name='inbox'),
    path('student_options', views.student_options, name='student_options'),
    path('all_assignments', views.all_assignments, name='all_assignments'),
    path('all_teachers', views.all_teachers, name='all_teachers'),
]
