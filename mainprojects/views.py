from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MainProject
from .forms import ProjectForm
from tasklist.models import Task


@login_required
def new(request):
    user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.added_by = user.username
            form.save()
            return redirect("welcome")
    else:
        form = ProjectForm()
    return render(request, "mainprojects/new.html", {"form": form, })


@login_required
def detail(request, id):
    proj = get_object_or_404(MainProject, pk=id)
    tasks = Task.objects.filter(main_project__id=id)
    return render(request, "mainprojects/detail.html", {"proj": proj, "tasks":tasks})


from django.shortcuts import render


