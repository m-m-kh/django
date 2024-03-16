from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class MyAccountView(generic.TemplateView):
    template_name = 'my_account.html'


def email(request):
    e = send_mail('me','heelow', settings.EMAIL_HOST_USER,['khademim217@gmail.com'],)
    print(e)
    return HttpResponse('sent')
