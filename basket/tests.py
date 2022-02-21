from django.urls import reverse
from django.test import TestCase, Client


class BasketViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_basket_get(self):
        url = reverse("view_basket")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shopping Basket")

