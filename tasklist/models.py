from django.db import models
import datetime
from mainprojects.models import MainProject

class Task(models.Model):
    title = models.CharField(max_length=100)
    main_project = models.ForeignKey(MainProject, on_delete = models.CASCADE)
    added_date = models.DateField(default = datetime.date.today)
    description = models.CharField(max_length=100)
    STATUS = (
        ('in pipeline', ('in pipeline')),
        ('done', ('done'))
    )
    status = models.CharField(max_length=20, choices=STATUS, default = 'in pipeline')
    added_by = models.CharField(max_length=100)
    PRIO = (
        ('low', ('low')),
        ('regular', ('regular')),
        ('high', ('high')),
    )
    prio = models.CharField(max_length=20, choices=PRIO, default = 'low')
    proceed_till = models.DateField(default = datetime.date.today)

    def overdue(self):
        if datetime.date.today() > self.proceed_till:
            return 'is overdue'
        elif datetime.date.today() < self.proceed_till:
            time_delta = str((self.proceed_till - datetime.date.today())).split(',')
            return f'you have still {time_delta[0]} left to complete this task'
        else:
            return 'It has to bo done today! Get to to work'





