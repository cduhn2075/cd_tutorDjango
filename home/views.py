from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"
