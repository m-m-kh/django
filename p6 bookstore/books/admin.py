from django.contrib import admin

from books.models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'user',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'datetime_created')
