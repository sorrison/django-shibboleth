from django.utils import unittest
from django.test.client import Client


class ShibbolethRegisterTestCase(unittest.TestCase):
    def test_invalid_attributes(self):
        client = Client()
        response = client.get('/login')
        self.assertEqual(403, response.status_code)
        self.assertTrue('shib_attrs' in response.context)

    def test_valid_attributes(self):
        client = Client()
        response = client.post('/login',
                              HTTP_SHIB_IDENTITY_PROVIDER='idp.test.com',
                              HTTP_SHIB_SHARED_TOKEN='3ho9qqthnbj0q0OE',
                              HTTP_SHIB_CN="Joe Blog",
                              HTTP_SHIB_MAIL="joe@test.com",
                              HTTP_SHIB_GIVENNAME="Joesph",
                              HTTP_SHIB_SN="Blog",
            )
        self.assertEqual(302, response.status_code, response.content)
        self.assertEqual("http://testserver/success", response["location"])
