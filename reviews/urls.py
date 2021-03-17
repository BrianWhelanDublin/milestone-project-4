from django.urls import path
from . import views


urlpatterns = [
    path("", views.our_reviews, name="our_reviews"),
    path("edit/<review_id>/", views.edit_review, name="edit_review"),
    path("delete/<review_id>/", views.delete_review, name="delete_review"),
]
