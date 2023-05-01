from django.shortcuts import render
from django.views.generic import TemplateView

#Builtin python imports
import json

#Django imports and third party imports
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
class CreateCheckoutSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        price_id = data.get("priceId")

        price_map = {
            'price_1N2kCiKOOXnQhQ0rzC5ODYwT': {'amount': 7500, 'currency': 'usd'},
            'price_1N2kBeKOOXnQhQ0rHaQyX4M7': {'amount': 13000, 'currency': 'usd'},
            'price_1N2kDTKOOXnQhQ0rdC8nTF9D': {'amount': 15000, 'currency': 'usd'},
        }

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": price_map[price_id]['currency'],
                            "product_data": {
                                "name": "Tutoring Plan",
                            },
                            "unit_amount": price_map[price_id]['amount'],
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=request.build_absolute_uri("/") + "?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri("/"),
            )
            return JsonResponse({"id": checkout_session.id})
        except Exception as e:
            return JsonResponse({"error": str(e)})

class SignUpView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = "tutorSignup/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context
