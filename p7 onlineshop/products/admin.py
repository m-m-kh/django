from django.contrib import admin

from products.models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin

class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ('author', 'product', 'text', )
    # readonly_fields = ('author',)
    # verbose_name = ''
    # verbose_name_plural = 'Commentsww'

@admin.register(Product)
class ProdctsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'datetime_created', 'datetime_modified')
    inlines = [
        CommentsInline,
    ]

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'datetime_created')


        
    
