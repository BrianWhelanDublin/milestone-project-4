from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (view_blog, view_post,
                        delete_comment, add_post,
                        edit_post, delete_post)


class TestUrls(SimpleTestCase):

    def test_view_blog_url(self):
        url = reverse("view_blog")
        self.assertEquals(resolve(url).func, view_blog)

    def test_view_post_url(self):
        url = reverse("view_post", args=["1"])
        self.assertEquals(resolve(url).func, view_post)

    def test_delete_comment_url(self):
        url = reverse("delete_comment", args=["1"])
        self.assertEquals(resolve(url).func, delete_comment)

    def test_add_post_url(self):
        url = reverse("add_post")
        self.assertEquals(resolve(url).func, add_post)

    def test_edit_post_url(self):
        url = reverse("edit_post", args=["1"])
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_post_url(self):
        url = reverse("delete_post", args=["1"])
        self.assertEquals(resolve(url).func, delete_post)
