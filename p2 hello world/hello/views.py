from django.shortcuts import render
from django.http import HttpResponse


def say_bye(request):
    return HttpResponse("bye")

