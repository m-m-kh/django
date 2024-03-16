from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'datetime_created')
    search_fields = ('title',)



# admin.site.register(Post)

