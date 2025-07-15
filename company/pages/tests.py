from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        respons = self.client.get("/")
        self.assertEqual(respons.status_code, 200)

    def the_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home")
        self.assertContains(response, "<H1>Welcome to Home Page</H1>")


class AboutPageTest(SimpleTestCase):
    def test_url_exsist_at_correct_location(self):
        respons = self.client.get("/about/")
        self.assertEqual(respons.status_code, 200)

    def the_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "abot")
        self.assertContains(response, "<H1>about page</H1>")
