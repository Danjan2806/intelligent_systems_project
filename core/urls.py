from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('presentations/', views.presentations_view, name='presentations'),
    path('project-management/', views.project_management_view, name='project_management'),
    path('documentation/', views.documentation_view, name='documentation'),
    path('testing/', views.testing_view, name='testing'),
]