from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detailproj'),
    path('new', views.new, name ='newproj')
]