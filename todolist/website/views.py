from django.shortcuts import render
from tasklist.models import Task

import operator

def welcome(request):
    tasks = Task.objects.all()
    return render(request, "website/welcome.html",
                  {"tasks":tasks})

def group_by(request, wish):
    tasks = Task.objects.all()
    if wish == 'project':
        ordered_by = sorted(tasks, key = operator.attrgetter('main_project.id'))
        return render(request, "website/welcome.html",
                  {"tasks":ordered_by})
    elif wish == 'completion':
        ordered_by = sorted(tasks, key=operator.attrgetter('proceed_till'))
        return render(request, "website/welcome.html",
                      {"tasks": ordered_by})
