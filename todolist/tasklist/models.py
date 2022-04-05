from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    added_date = models.DateField(default = date.today)
    description = models.CharField(max_length=100)
    STATUS = (
        ('in pipeline', ('work in progress')),
        ('done', ('task completed'))
    )
    status = models.CharField(max_length=20, choices=STATUS, default = 'in pipeline')
    added_by = models.CharField(max_length=100)

    @property
    def is_overdue(self):
        if self.added_date > (date.today + date.timedelta(days=7)):
            return True
        return False



