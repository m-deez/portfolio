from django.urls import path
from . import views


urlpatterns = [
    path('', views.About.as_view(), name='about'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/bja/', views.BlackJackAttack.as_view(), name='bja'),
    path('projects/wc/', views.WondrousCreations.as_view(), name='wc'),
    path('projects/as/', views.AlleyScoop.as_view(), name='as'),
    path('projects/pw/', views.ProjectWayfarer.as_view(), name='pw'),
    path('projects/pon/', views.PlentyOfNerds.as_view(), name='pon'),
]