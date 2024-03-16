from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestSignUp(TestCase):
    def test_signup_url(self):
        cl = self.client.get(reverse('signup'))
        self.assertEqual(cl.status_code, 200)
        cl = self.client.get('/accounts/signup/')
        self.assertEqual(cl.status_code, 200)

    def test_signup_form(self):
        cl = self.client.post(reverse('signup'),{'username':'ali',
                                                 'password1':'khademim0903',
                                                 'password2':'khademim0903'})
        self.assertEqual(cl.status_code,302)
        self.assertEqual(cl.url,reverse('login'))
        user = get_user_model().objects.all()
