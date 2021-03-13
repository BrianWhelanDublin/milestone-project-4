from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("previous_order/<order_number>",
         views.previous_order, name="previous_order"),
]
