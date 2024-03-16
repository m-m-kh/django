from django.urls import path
from .views import say_bye


urlpatterns = [
    path('hi/', say_bye, name="bye")
]