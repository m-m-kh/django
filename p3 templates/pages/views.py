from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    context = {
        "name":"soha"
    }
    return render(request, 'about.html', context=context)


def contactus_page_view(request):
    return render(request, 'contactus.html')
