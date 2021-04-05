from django.test import TestCase, Client
from blog.models import Post, Comment
from django.contrib.auth.models import User


class TestBlogModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

    def test_post_model(self):
        post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="Test Content",
            image="test_image.jpg",
        )
        self.assertEqual(str(post), "Test Post")

    def test_comment_model(self):
        self.client.login(
            username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test Post",
            author=self.user,
            content="Test Content",
            image="test_image.jpg",
        )
        comment = Comment.objects.create(
            post=post,
            author=self.user,
            comment="Test Comment",
        )
        self.assertEqual(str(comment), "Comment on Test Post by testuser")
