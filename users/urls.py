from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_profile, name="user_profile")
]