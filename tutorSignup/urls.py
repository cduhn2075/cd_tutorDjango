
from django.urls import path
from .views import SignUpView, CreateCheckoutSessionView
from django.contrib.auth.decorators import login_required

urlpatterns = [


    path('', login_required(SignUpView.as_view()), name='signup'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),


]