from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def gettask(request):
    return render(request, 'tasks/task.html')


def send_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            priority = form.cleaned_data['priority']
            duration = form.cleaned_data['duration']
            due_time = form.cleaned_data['due_time']
            t = Task(name=name, priority=priority, duration=duration, due_time=due_time)
            t.save()
            return HttpResponseRedirect('/home/')
    else:
        form = TaskForm()
    return render(request, 'home.html', {'form': form})

