from django.forms import ModelForm
from django import forms
from books.models import Book, Comment


class BookForm(ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={"maxlength": "33"}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'intro', 'price', 'cover',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        # fields = '__all__'