from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import NewPostForm
from django.http import HttpResponse


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(title='Test title',
                                         text='Test content',
                                         status=Post.STATUS[0][0],
                                         author=cls.user)
        cls.post2 = Post.objects.create(title='Test title2',
                                         text='Test content2',
                                         status=Post.STATUS[1][0],
                                         author=cls.user)

    def test_url_post_list_by_name(self):
        client = self.client.get(reverse('post_list'))
        self.assertEquals(client.status_code, 200)

    def test_url_post_view_by_name(self):
        client = self.client.get(reverse('post_list'))
        self.assertEquals(client.status_code, 200)

    def test_post_list(self):
        client = self.client.get(reverse('post_list'))
        self.assertContains(client, self.post1.title)
        self.assertContains(client, self.post1.text)

    def test_post_list_by_name(self):
        client = self.client.get(reverse('post_list'))
        posts = Post.objects.filter(status='drf')
        for post in posts:
            self.assertNotContains(client, post.title)
            self.assertNotContains(client, post.text)

    def test_new_post_url(self):
        client = self.client.get(reverse('new_post'))
        self.assertEquals(client.status_code,200)

    def test_new_post_insert_data(self):
        data = {
            'title': 'Test title3',
            'text': 'Test content3',
            'status': Post.STATUS[1][0],
            'author': self.user.pk}
        cl = self.client.post(reverse('new_post'), data)

        self.assertEquals(cl.status_code, 302)
        self.assertEquals(Post.objects.last().title, 'Test title3')
        self.assertEquals(Post.objects.last().text, 'Test content3')
        self.assertEquals(Post.objects.last().status, Post.STATUS[1][0])
        self.assertEquals(Post.objects.last().author, self.user)

    def test_delete_post(self):
        self.client.post(reverse('post_delete', args=[self.post1.pk]))
        cl = self.client.get(reverse('post_list'))
        self.assertNotContains(cl, self.post1.title)
