from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    # success_url = reverse_lazy('post_list')
    def get_success_url(self):
        return reverse('post_list')
