from django.test import TestCase
from stock.models import Category, Item


class TestStockModels(TestCase):

    def test_category_model(self):
        category = Category.objects.create(
            name="test_category",
            display_name="Test Category",
        )
        self.assertEqual(str(category), "test_category")

    def test_item_model(self):
        category = Category.objects.create(
            name="test_category",
            display_name="Test Category",
        )
        item = Item.objects.create(
            code="1",
            name="test item",
            description="test description",
            price="2.99",
            image="testimage.jpg",
            category=category,
        )
        self.assertEqual(str(item), "test item")
