from django import template
from django.forms import ModelForm

register = template.Library()


@register.filter
def to_upper(value):
    return value.upper()

@register.filter
def enter(value:ModelForm):

    v = value.fields['title'].widget.attrs.get('maxlength')
    value.fields['title'].widget.attrs.update({'maxlength':f'22 {v}'})
    # value = value.replace('\r', '\n<br>')
    return value