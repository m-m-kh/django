from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_view'),
    path('new_post', views.PostCreate.as_view(), name='new_post'),
    path('post/edit/<int:pk>', views.PostUpdate.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
]