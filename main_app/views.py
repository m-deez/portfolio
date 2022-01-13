from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ProjectList(TemplateView):
    template_name = "project_list.html"

class BlackJackAttack(TemplateView):
    template_name = "bja.html"

class WondrousCreations(TemplateView):
    template_name = "wc.html"

class AlleyScoop(TemplateView):
    template_name = "as.html"

class ProjectWayfarer(TemplateView):
    template_name = "pw.html"

class PlentyOfNerds(TemplateView):
    template_name = "pon.html"