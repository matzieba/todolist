from django.urls import path

from . import views

urlpatterns =[
    path('group_by/<str:wish>', views.group_by, name='group_by'),
    path('', views.welcome, name='welcome'),
]