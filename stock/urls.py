from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_items, name="all_items"),
    path("<int:item_id>/", views.single_item, name="single_item"),
    path("add/item/", views.add_item, name="add_item"),
    path("edit/item/<int:item_id>/", views.edit_item, name="edit_item"),
    path("delete/item/<int:item_id>/", views.delete_item, name="delete_item"),
]
