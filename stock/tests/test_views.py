from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from stock.forms import ItemForm
from stock.models import Item, Category
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import base64


class TestStockViews(TestCase):
    "test the stock views for all users"

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            display_name="Test Category"
        )
        self.item = Item.objects.create(
            code="1",
            name="test item",
            description="test description",
            price="2.99",
            image="testimage.jpg",
            category=self.category,
        )
        self.all_items = reverse("all_items")
        self.single_item = reverse("single_item",
                                   kwargs={"item_id": self.item.id})

    def test_all_items_view(self):
        response = self.client.get(self.all_items)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/all_items.html")
        self.assertTemplateUsed(response, "base.html")

    def test_all_items_views_with_query(self):
        response = self.client.get(self.all_items,
                                   {"query": "test"})

        context = response.context
        self.assertTrue(context['search'])
        self.assertEqual(context['search'], 'test')

    def test_all_items_views_with_empty_query(self):
        response = self.client.get(self.all_items,
                                   {"query": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "No search query entered.")

    def test_all_items_views_with_category(self):
        response = self.client.get(self.all_items,
                                   {"category": "test_category"})
        category = Category.objects.get(name="test_category")
        context = response.context
        self.assertTrue(context['current_category'])
        self.assertEqual(context['current_category'], category)

    def test_all_items_views_with_sort(self):
        response = self.client.get(self.all_items,
                                   {"sort": "name"})
        context = response.context
        self.assertTrue(context['sort'])
        self.assertEqual(context['sort'], "name")

    def test_all_items_views_with_direction(self):
        response = self.client.get(self.all_items,
                                   {"sort": "name",
                                    "direction": "desc"})
        context = response.context
        self.assertTrue(context['direction'])
        self.assertEqual(context['direction'], "desc")
    
    def test_view_single_item_view(self):
        response = self.client.get(self.single_item)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/item.html")
        self.assertTemplateUsed(response, "base.html")
