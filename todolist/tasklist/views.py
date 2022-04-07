from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def new(request):
    user = request.user
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.added_by = user.username
            form.save()
            return redirect("welcome")
    else:
        form = TaskForm()
    return render(request, "tasklist/new.html", {"form":form,})

@login_required
def detail(request, id):
    task = get_object_or_404(Task, pk = id)
    return render(request, "tasklist/detail.html", {"task":task})


