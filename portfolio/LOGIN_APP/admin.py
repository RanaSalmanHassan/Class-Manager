from django.contrib import admin
from .models import User,TeacherProfile,StudentProfile,Message
# Register your models here.
admin.site.register(User)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(Message)
