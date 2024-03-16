from django.urls import path

from . import views


urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books_list'),
    # path('books/', views.BookListPerPageView.as_view(), name='books_list_per_page'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='books_detail'),
    # path('books/<int:pk>', views.book_detail, name='books_detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/edit/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('books/my_books/', views.MyBookListView.as_view(), name='my_books'),
]