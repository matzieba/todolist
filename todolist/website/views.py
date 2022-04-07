from django.shortcuts import render
from tasklist.models import Task
import datetime

def welcome(request):
    date = datetime.date.today()
    return render(request, "website/welcome.html",
                  {"tasks":Task.objects.all(), "date":date},)
