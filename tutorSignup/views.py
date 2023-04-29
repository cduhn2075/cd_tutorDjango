from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "tutorSignup/signup.html"