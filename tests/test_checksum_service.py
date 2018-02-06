__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.checksum import Checksum
from paymill.models.address import Address
from paymill.models.shopping_cart_item import ShoppingCartItem
from . import test_config


class TestChecksumService(unittest.TestCase):

    def setUp(self):
        self.p = PaymillContext(test_config.api_key)

    def tearDown(self):
        del self.p

    def test_create_default_checksum_for_paypal(self):
        cs = self.p.checksum_service.create(checksum_type='paypal', amount=1234, currency='EUR', return_url='http://test.com/success',
                                           cancel_url='http://test.com/failure')
        self.assertIsInstance(cs, Checksum)
        self.assertNotEquals(None, cs.id)

    def test_create_default_checksum_for_paypal_with_address(self):
        ad = Address(name="Max Mustermann",
                    street_address="Musterstr. 1",
                    street_address_addition="",
                    city="Munich", state="Bavaria",
                    postal_code="80333", country="DE",
                    phone="+4989123456")

        cs = cs = self.p.checksum_service.create(checksum_type='paypal', amount=1234, currency='EUR', return_url='http://test.com/success',
                                           cancel_url='http://test.com/failure', shipping_address=ad)
        self.assertIsInstance(cs, Checksum)
        self.assertNotEquals(None, cs.id)

    def test_create_default_checksum_for_paypal_with_shopping_cart(self):
        sc1 = ShoppingCartItem(name="Sample Product 1",
                          description="Amazing product used as an example",
                          item_number="PRD12345",
                          url="https://www.example.com/shop/products/12345",
                          amount=1000,
                          quantity=3)

        sc2 = ShoppingCartItem(name="Sample Product 2",
                          description="Amazing product used as an example",
                          item_number="PRD12346",
                          url="https://www.example.com/shop/products/12346",
                          amount=9999,
                          quantity=12)

        items = [sc1, sc2]

        cs = self.p.checksum_service.create(checksum_type='paypal', amount=1234, currency='EUR', return_url='http://test.com/success',
                                           cancel_url='http://test.com/failure', items=items)

        self.assertIsInstance(cs, Checksum)
        self.assertNotEquals(None, cs.id)

    def test_create_default_checksum_for_paypal_with_checkout_options(self):
        co_opts = dict(shipping_address_editable=True)

        cs = self.p.checksum_service.create(checksum_type='paypal', amount=1234, currency='EUR', return_url='http://test.com/success',
                                           cancel_url='http://test.com/failure', checkout_options=co_opts)

        self.assertIsInstance(cs, Checksum)
        self.assertNotEquals(None, cs.id)
