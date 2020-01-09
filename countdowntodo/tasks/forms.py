from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class TaskForm(forms.Form):
    task_name = forms.CharField(max_length=64, required=True)
    task_priority = forms.IntegerField(required=False)
    task_duration = forms.DurationField()
    task_due_time = forms.DateField(required=False, input_formats=['%d-%m-%Y'])

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ('name', 'priority', 'duration', 'due_time')

