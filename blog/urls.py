from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_blog, name="view_blog"),
    path("post/<int:post_id>/", views.view_post, name="view_post"),
    path("post/<int:post_id>delete/comment/",
         views.delete_comment, name="delete_comment"),
    path("add/post/", views.add_post, name="add_post"),
    path("edit/post/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/post/<int:post_id>/", views.delete_post, name="delete_post"),
]
