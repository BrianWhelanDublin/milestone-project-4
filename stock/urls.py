from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_items, name="all_items"),
    path("<int:item_id>/", views.single_item, name="single_item"),
]
