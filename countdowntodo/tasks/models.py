from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField('Task Name', max_length=120)
    priority = models.CharField(max_length=120)
    duration = models.CharField(max_length=60)
    due_time = models.DateTimeField('Task Due Time')

    class Meta:
        app_label = 'tasks'

    def __str__(self):
        return self.name
