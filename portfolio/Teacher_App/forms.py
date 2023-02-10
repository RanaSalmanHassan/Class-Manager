from django import forms
from .models import Assignment,Notice_to_Students

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ('teacher',)


class Notice_to_Students_Form(forms.ModelForm):
    class Meta:
        model = Notice_to_Students
        exclude = ('teacher',)
