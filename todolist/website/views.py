from django.shortcuts import render
from tasklist.models import Task

def welcome(request):
    return render(request, "website/welcome.html",
                  {"tasks":Task.objects.all()})
