from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE,related_name='teacher_profile')
    profile_pic = models.ImageField(upload_to='teacher_profile',blank=True)
    contact_num = models.CharField(max_length=11)
    subject = models.CharField(max_length=70)
    role = models.CharField(max_length=50)  # Teacher`s Role e.g. Principal,Coordinator


class StudentProfile(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')
    profile_pic = models.ImageField(upload_to='student_profile',blank=True)
    contact_num = models.CharField(max_length=11)