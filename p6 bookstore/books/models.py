from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    intro = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='my_books')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('book_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('book_delete', args=[self.pk])


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.book.pk])
