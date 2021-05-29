from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from stock.models import Item, Category


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
            price=2.99,
            image="testimage.jpg",
            category=self.category,
        )
        self.all_items = reverse("all_items")
        self.single_item = reverse("single_item",
                                   kwargs={"item_id": self.item.id})

    def test_all_items_view(self):
        ''' Test the all items view '''

        response = self.client.get(self.all_items)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/all_items.html")
        self.assertTemplateUsed(response, "base.html")

    def test_all_items_views_with_query(self):
        ''' Test the all items view with a query parameter '''

        response = self.client.get(self.all_items,
                                   {"query": "test"})
        context = response.context
        self.assertTrue(context['search'])
        self.assertEqual(context['search'], 'test')

    def test_all_items_views_with_empty_query(self):
        '''  Test the all items view with an empty query '''

        response = self.client.get(self.all_items,
                                   {"query": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "No search query entered.")

    def test_all_items_views_with_category(self):
        ''' Test the all items view with a category parameter '''

        response = self.client.get(self.all_items,
                                   {"category": "test_category"})
        category = Category.objects.get(name="test_category")
        context = response.context
        self.assertTrue(context['current_category'])
        self.assertEqual(context['current_category'], category)

    def test_all_items_views_with_sort(self):
        '''  Test the all items view with a sort paramater '''

        response = self.client.get(self.all_items,
                                   {"sort": "name"})
        context = response.context
        self.assertTrue(context['sort'])
        self.assertEqual(context['sort'], "name")

    def test_all_items_views_with_direction(self):
        ''' Test the all items view with a direction parameter '''

        response = self.client.get(self.all_items,
                                   {"sort": "name",
                                    "direction": "desc"})
        context = response.context
        self.assertTrue(context['direction'])
        self.assertEqual(context['direction'], "desc")

    def test_view_single_item_view(self):
        ''' Test the single item view '''
        response = self.client.get(self.single_item)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/item.html")
        self.assertTemplateUsed(response, "base.html")


class TestStockControl(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.super_user = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@email.com',
            password='testadminpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            display_name="Test Category"
        )
        self.item = Item.objects.create(
            code="1",
            name="test item",
            description="test description",
            price=2.99,
            image="testimage.jpg",
            category=self.category,
        )
        self.all_items = reverse("all_items")
        self.single_item = reverse("single_item",
                                   kwargs={"item_id": self.item.id})
        self.add_item = reverse("add_item")
        self.home_page = reverse("home_page")
        self.edit_item = reverse("edit_item", kwargs={"item_id": self.item.id})
        self.delete_item = reverse("delete_item",
                                   kwargs={"item_id": self.item.id})

    def test_add_item_not_supperuser(self):
        ''' Test the add item view if the user is not a superuser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.add_item)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_add_item_GET_supperuser(self):
        ''' Test the add item get if not a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.add_item)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/add_item.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_add_item_POST_invalidform(self):
        ''' Test the add item with an invalid form '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.add_item, {
            "code": "",
            "name": "",
            "description": "",
            "price": "",
            "category": self.category,
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Failed to add the item. \
    Please check the form details are correct and try again.")

    def test_add_item_POST_validform(self):
        ''' test the add item with a valid form '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.add_item, {
            "name": "Test",
            "description": "test description",
            "price": 2.99,
         })
        item = Item.objects.get(name="Test")
        self.assertTrue(item)
        self.assertEqual(item.description, 'test description')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Item has been added successfully.")

    def test_edit_post_if_not_superuser(self):
        ''' Test the edit post view if not a superuser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.edit_item)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_edit_item_GET_if_superuser(self):
        ''' Test the edit item get if superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.edit_item)
        self.assertEqual(response.context['form'].initial['name'],
                         self.item.name)
        self.assertEqual(response.context['form'].initial['description'],
                         self.item.description)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stock/edit_item.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/nav-background.html")

    def test_edit_item_POST_invalidform(self):
        ''' test the edit item view post with invalid form'''

        self.client.login(
            username="testadmin", password="testadminpassword")

        response = self.client.post(self.edit_item, {

        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Failed to update item.\
  Please check the form details are correct and try again.")

    def test_edit_item_POST_validform(self):
        ''' Test edit item view with a valid form '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.edit_item, {
            "name": "Test editing",
            "description": "test description edited",
            "price": 100.00,
            }
        )
        item = Item.objects.get(id=self.item.id)
        self.assertEqual(item.description, 'test description edited')
        self.assertEqual(item.price, 100.00)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Item update successfully")

    def test_delete_item_if_not_superuser(self):
        ''' Test delete item view if not a superuser '''

        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.delete_item)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_post_GET_if_superuser(self):
        ''' Test delete item view if a superuser '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.get(self.delete_item)
        self.assertRedirects(response, self.home_page)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You do not have permission to do this.")

    def test_delete_item_POST(self):
        ''' Test the delete post post POST function '''

        self.client.login(
            username="testadmin", password="testadminpassword")
        response = self.client.post(self.delete_item)
        item = Item.objects.filter(id=self.item.id)
        self.assertFalse(item)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Product has been deleted")
