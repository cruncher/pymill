__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.utils.http_client import HTTPClient


class TestHTTPClient(unittest.TestCase):
    """

    Testing all local methods of the HTTPClient abstraction

    """

    api_key = '20a690e5283cd3419629a42cc8631193'
    api_url = 'https://api.paymill.com/v2.1'

    def setUp(self):
        self.http_client = HTTPClient(TestHTTPClient.api_url, TestHTTPClient.api_key)

    def test_client_init(self):
        c = HTTPClient(self.api_url, self.api_key)
        self.assertIsInstance(c, HTTPClient)

    def test_client_init_sets_url(self):
        self.assertEqual(
            self.http_client.base_url, TestHTTPClient.api_url)

    def test_client_init_sets_user_and_pass(self):
        self.assertEqual(self.http_client.session.auth, (TestHTTPClient.api_key, ''))



