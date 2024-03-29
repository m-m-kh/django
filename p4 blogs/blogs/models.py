from django.db import models
from django.urls import reverse

class Post(models.Model):
    STATUS = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=3)

    def get_absolute_url(self):
        return reverse('post_view', args=[self.pk])