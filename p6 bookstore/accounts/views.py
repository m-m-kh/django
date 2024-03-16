from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView
from . import forms
from . import models


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
