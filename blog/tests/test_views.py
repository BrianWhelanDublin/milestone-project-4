from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from blog.models import Post, Comment

from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import base64
import tempfile


class TestBlogPostViews(TestCase):
    ''' test the blog views for all users '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="Test Content",
            image="test_image.jpg",
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            comment="Test Comment",
        )
        self.view_blog = reverse("view_blog")
        self.view_post = reverse("view_post",
                                 kwargs={"post_id": self.post.id})
        self.delete_comment = reverse("delete_comment",
                                      kwargs={"post_id": self.post.id})

    def test_view_blog_view_GET(self):
        ''' Test the view blog view '''

        response = self.client.get(self.view_blog)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/view_blog.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_view_post_GET(self):
        ''' test the view post view with a GET request '''

        response = self.client.get(self.view_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_view_post_POST_form_valid(self):
        ''' test the view post view with a POST request
            and a valid form '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.post(self.view_post,
                                    {"comment": "Test Comment"})
        self.assertRedirects(response, self.view_post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your comment has been added.")

    def test_view_post_POST_form_invalid(self):
        ''' test the view post view with a POST request
            and an invalid form '''

        response = self.client.post(self.view_post,
                                    {"": ""})
        self.assertRedirects(response, self.view_post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error adding your comment please try again")


class TestBlogCommentsViews(TestCase):
    ''' test the views that include comments functionality '''

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="Test Content",
            image="test_image.jpg",
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            comment="Test Comment",
        )
        self.view_post = reverse("view_post",
                                 kwargs={"post_id": self.post.id})
        self.delete_comment = reverse("delete_comment",
                                      kwargs={"post_id": self.post.id})

    def test_delete_comment_view_POST(self):
        ''' test the delete comment view '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.post(self.delete_comment,
                                    {"comment_id": self.comment.id})
        self.assertRedirects(response, self.view_post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Your comment has been deleted.")

    def test_delete_comment_view_POST_exception(self):
        ''' test the delete comment view exception'''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.post(self.delete_comment,
                                    {"comment_id": "2"})
        self.assertRedirects(response, self.view_post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error deleteing your comment")

    def test_delete_comment_view_GET(self):
        ''' test the GET response if the user tries to
        type the URL into the browser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.delete_comment)
        self.assertRedirects(response, self.view_post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error you do not have \
permission to do this.")


class TestPostSuperuserViews(TestCase):
    ''' test the views for the superuser to add
       posts, edit posts, and delete posts '''

    def setUp(self):
        self.client = Client()
        self.super_user = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@email.com',
            password='testadminpassword'
        )
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="Test Content",
            image="test_image.jpg",
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            comment="Test Comment",
        )
        self.add_post = reverse("add_post")
        self.edit_post = reverse("edit_post", kwargs={"post_id": self.post.id})
        self.delete_post = reverse("delete_post",
                                   kwargs={"post_id": self.post.id})
        self.view_blog = reverse("view_blog")
        self.view_post = reverse("view_post", kwargs={"post_id": self.post.id})

    def test_add_post_if_not_superuser(self):
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.add_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_add_post_GET_if_superuser(self):
        ''' test the add post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.get(self.add_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_post.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_add_post_POST_invalidform(self):
        ''' test the add post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.add_post, {
            "title": "Test Post",
            "content": "Test Content",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Failed to add the post. \
Please check the form details are correct and try again.")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_add_post_POST_validform(self):
        ''' test the add post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")

        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )

        response = self.client.post(self.add_post, {
            "title": "Test Adding Post",
            "content": "Test adding content",
            "image": image,
            }
        )
        post = Post.objects.get(title="Test Adding Post")
        self.assertTrue(post)
        self.assertEqual(post.content, 'Test adding content')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Post has been added successfully.")

    def test_edit_post_if_not_superuser(self):
        ''' test the edit post view if a user isnt a superuser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.edit_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_edit_post_GET_if_superuser(self):
        ''' test the edit post view get if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.edit_post)
        self.assertEqual(response.context['form'].initial['title'],
                         self.post.title)
        self.assertEqual(response.context['form'].initial['content'],
                         self.post.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/add_post.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_edit_post_POST_invalidform(self):
        ''' test the edit post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.edit_post, {

        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Failed to edit the post. \
Please check the form details are correct and try again.")

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_edit_post_POST_validform(self):
        ''' test the edit post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")

        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )

        response = self.client.post(self.edit_post, {
            "title": "Test Post",
            "content": "Test editing content",
            "image": image,
            }
        )
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.content, 'Test editing content')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Post updated successfully")

    def test_delete_post_if_not_superuser(self):
        ''' test the delete post view if a user isnt a superuser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.delete_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_post_GET_if_superuser(self):
        ''' test the delete post view GET if the user is a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.delete_post)
        self.assertRedirects(response, self.view_blog)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_post_POST(self):
        ''' Test the delete post POST function '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.delete_post)
        post = Post.objects.filter(id=self.post.id)
        self.assertFalse(post)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Post has been deleted")


TEST_IMAGE = '''
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
'''.strip()
