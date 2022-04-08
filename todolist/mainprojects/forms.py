from django.forms import ModelForm
from .models import MainProject

class ProjectForm(ModelForm):
    class Meta:
        model = MainProject
        exclude = ['added_by']
