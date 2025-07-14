from django.test import TestCase


# Create your tests here.
from django.test import SimpleTestCase


class Homepagetest(SimpleTestCase):
    def test(self):
        respons = self.client.get("/")
        self.assertEqual(respons.status_code, 200)


class Aboutpagetest(SimpleTestCase):
    def test(self):
        respons = self.client.get("/about/")
        self.assertEqual(respons.status_code, 200)
