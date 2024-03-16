from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Book, Comment
from .forms import BookForm, CommentForm
from django.shortcuts import get_object_or_404, redirect

from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'data'
    paginate_by = 5

# class BookListView(generic.ListView):
#     model = Book
#     template_name = 'books/books_list.html'
#     context_object_name = 'data'
#
#     def get_queryset(self):
#         page = int(self.request.GET.get('name',1))
#         queryset = Book.objects.all()
#         self.kwargs['len_page'] = list(range(1,int((len(queryset)/5)+1)+1))
#         return queryset[(page-1)*5:page*5]
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['len_page'] = self.kwargs['len_page']
#         return context
#
#     def get(self, *args, **kwargs):
#         if not self.get_queryset():
#             raise Http404()
#         return super().get(*args, **kwargs)




class BookDetailView(generic.CreateView, generic.DetailView):
    model = Book
    template_name = 'books/books_detail.html'
    context_object_name = 'data'
    form_class = CommentForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.book = self.get_object()
        form.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books_detail', args={self.kwargs['pk']})



# @login_required
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     comments = book.comments.all()
#
#     form = CommentForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.book = book
#             try:
#                 form.user = request.user
#             except:
#                 return redirect('login')
#             form.save()
#             form = CommentForm()
#
#     return render(request, 'books/books_detail.html',
#                   context={'data': book,
#                            'comments': comments,
#                            'form': form})


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/books_detail.html'
#     context_object_name = 'data'
#
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['comments'] = Comment.objects.filter(book=self.object)
#         # context['data'] = Book.objects.get(pk=self.kwargs['pk'])
#         return context


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         form = BookForm()
    #         return render(request, 'books/book_create.html', context={'form':form})
    #
    #     return redirect(reverse('login')+'?next='+reverse('book_create'))
    # model = Book
    # fields = '__all__'
    form_class = BookForm
    template_name = 'books/book_create.html'

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = self.request.user
            form.save()
            return redirect(form.get_absolute_url())

        return render(request, self.template_name, {'form': form})




class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books_list')

    def test_func(self):
        return self.get_object().user == self.request.user

class BookDeleteView(generic.DeleteView):
    model = Book
    context_object_name = 'data'
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')

class MyBookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'books/my_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return self.request.user.my_books.all()

