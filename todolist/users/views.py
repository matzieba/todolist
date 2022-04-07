from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib import messages


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        messages.add_message(request, messages.INFO, 'This username is already taken. Please choose another one!')
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create user and save to the database
            try:
                user = User.objects.create_user(
                    form.cleaned_data["your_name"],
                    form.cleaned_data["your_email"],
                    form.cleaned_data["your_password"],
                )
            # user.username =
            # user.email =
            # user.password =
                user.save()
            except:
                return redirect("register")
        return redirect("welcome")
    return render(request, "register.html", {"form":form})
