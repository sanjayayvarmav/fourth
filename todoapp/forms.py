from django import forms

from todoapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ['name','priority','date']

