from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/bja/', views.BlackJackAttack.as_view(), name='bja'),
    path('projects/wc/', views.WondrousCreations.as_view(), name='wc'),
]