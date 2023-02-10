from django.db import models
from LOGIN_APP.models import User
from LOGIN_APP.models import TeacherProfile
# Create your models here.
class Assignment(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher_assigner')
    title = models.CharField(max_length=100)
    assignment = models.FileField(upload_to='assignments')
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.teacher} sent this assignment on {self.date_added}')

class Notice_to_Students(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher_notice')
    notice = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.teacher} wrote this notice on {self.date_added}')