from django.urls import path
from .views import HomeView, ContactView, SupportView
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', login_required(HomeView.as_view()), name='home'),
    path('contact/', login_required(ContactView.as_view()), name='contact'),
    path('support/', login_required(SupportView.as_view()), name='support'),


]