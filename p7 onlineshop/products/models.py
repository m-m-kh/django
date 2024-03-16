from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone
from ckeditor.fields import RichTextField
class ActiveProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    # cover = models.ImageField(upload_to='products_image/')
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()
    active = models.BooleanField(default=True)


    # managers
    objects = models.Manager()
    active_product = ActiveProduct()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name= _('text'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.pk])

    class Meta:
        # verbose_name = "کامنت"
        verbose_name_plural = "کامنت"
