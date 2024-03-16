from . import forms
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
class SignUp(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('signup')



