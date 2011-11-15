from django.utils import unittest
from django.test.client import Client


class ShibbolethRegisterTestCase(unittest.TestCase):
    def test_invalid_attributes(self):
        client = Client()
        response = client.get('/login')
        self.assertTrue('shib_attrs' in response.context)
        self.assertEqual(403, response.status_code)
