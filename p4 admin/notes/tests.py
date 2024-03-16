from django.test import TestCase
from django.urls import reverse
from . import models

class TestNotesView(TestCase):
    
    def test_url_status(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_status_by_name(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_text_view(self):
        models.Note.objects.create(name="ali",text="hello")
        response = self.client.get(reverse('note_list'))
        self.assertContains(response,'ali')
        