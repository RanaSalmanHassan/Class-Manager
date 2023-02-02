from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField()
    is_student = models.BooleanField()


class TeacherProfile(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher_profile')
    profile_pic = models.ImageField(upload_to='teacher_profile')
    contact_num = models.CharField(max_length=11)
    subject = models.CharField(max_length=70)
    role = models.CharField(max_length=50)  # Teacher`s Role e.g. Principal,Coordinator


class StudentProfile(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_profile')
    profile_pic = models.ImageField(upload_to='student_profile')
    contact_num = models.CharField(max_length=11)