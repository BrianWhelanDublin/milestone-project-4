from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("ourstory/", views.our_story, name='our_story'),
    path("contact/", views.contact, name='contact'),
]
