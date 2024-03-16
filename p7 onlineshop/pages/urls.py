from django.urls import path
from . import views


urlpatterns = [
    path('my_account/', views.MyAccountView.as_view(), name='my_account'),
    path('email', views.email),
]