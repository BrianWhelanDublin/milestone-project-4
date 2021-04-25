from django.test import TestCase
from checkout.models import Order, OrderLineItem
from stock.models import Item


class TestCheckoutModels(TestCase):

    def test_order_model(self):
        ''' test the order model '''
        order = Order.objects.create(
            full_name="Test User"
        )

        self.assertEqual(str(order), order.order_number)

    def test_orderlineitem_model(self):
        ''' test the orderlineitem model '''

        order = Order.objects.create(
            full_name="Test User"
        )

        item = Item.objects.create(
            name='Test Product',
            price=100,
            code=123,
        )

        order_line_item = OrderLineItem.objects.create(
            order=order,
            item=item,
            quantity=1,
            lineitem_total=100,
        )

        self.assertEqual(str(order_line_item),
                         f"Code: 123 on order {order.order_number}")
