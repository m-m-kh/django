from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.payment_process, name='payment_process'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
]