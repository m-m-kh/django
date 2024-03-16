from django.urls import path
from . import views

# app_name = 'cart'

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('update_cart/<int:pk>/', views.update_cart, name='update_cart'),
    path('remove_cart/<int:pk>/', views.remove_cart, name='remove_cart'),
    path('remove_all_cart/', views.remove_all_cart, name='remove_all_cart'),
]