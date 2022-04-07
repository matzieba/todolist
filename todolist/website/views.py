from django.shortcuts import render
from tasklist.models import Task
import datetime
import operator

def welcome(request):
    date = datetime.date.today()
    tasks = Task.objects.all()
    ordered_by = sorted(tasks, key = operator.attrgetter('title'))
    return render(request, "website/welcome.html",
                  {"tasks":ordered_by, "date":date},)

