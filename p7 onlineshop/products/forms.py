from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from django import forms
from .models import Comment


class CommentForm(ModelForm):
    # text = RichTextField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        fields = ('text',)
