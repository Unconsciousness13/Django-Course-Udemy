from django.urls import path
from . import views


urlPatterns = [
    path('projects/',views.projects, name="projects"),
    path('project/',views.project, name="single project"),
    path('projectPlus/<str:pk>/',views.projectPlus, name="single project")
]