from django.test import TestCase

# Create your tests here.
from .models import post
from django.urls import reverse


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = post.objects.create(text="this is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "this is a test")

    def test_home_page_avalibel(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_avalibel_by_name(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "post_list.html")

    def test_template_content(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, "Post List Home Page")
