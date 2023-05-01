from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = "home/home.html"




class ContactView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = "home/contact.html"


class SupportView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = "home/support.html"
