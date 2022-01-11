from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/1/', views.BlackJackAttack.as_view(), name='bja'),
]