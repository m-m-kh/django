from django.test import TestCase
from django.urls import reverse


class PagesTest(TestCase):
    def test_home_page(self):
        cli = self.client.get(reverse('home'))
        self.assertEqual(cli.status_code, 200)
        self.assertTemplateUsed('home')
        self.assertContains(cli, 'hello')
