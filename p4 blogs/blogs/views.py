from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from . import models
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse
# Create your views here.
# def post_list(request):
#     data = models.Post.objects.filter(status='pub').order_by('-datetime_modified')
#     # data = models.Post.objects.all()
#     context = {'data': data}
#     return render(
#         request, 'home.html', context=context
#     )

class PostList(generic.ListView):
    # model = models.Post
    template_name = 'home.html'
    # ordering = ['-datetime_modified']
    context_object_name = 'data'

    def get_queryset(self):
        return models.Post.objects.filter(status='pub').order_by('-datetime_modified')


# def post_view(request, pk):
#     # data = get_object_or_404(models.Post, pk=pk)
#     try:
#         data = models.Post.objects.get(pk=pk)
#         context = {'data': data}
#         return render(
#             request, 'post_detail.html', context=context
#         )
#     except models.Post.DoesNotExist:
#         return HttpResponse('404')

class PostDetail(generic.DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'data'
    model = models.Post


# def new_post(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = NewPostForm()
#             return redirect('post_list')
#     else:
#         form = NewPostForm()
#     return render(request, 'new_post.html', context={'form': form})

class PostCreate(generic.CreateView):
    template_name = 'new_post.html'
    form_class = NewPostForm
    context_object_name = 'data'
    #
    # def get_success_url(self):
    #     return reverse('post_view')


# def post_edit(request, pk):
#     data = models.Post.objects.get(pk=pk)
#     form = NewPostForm(request.POST or None, instance=data)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")
#     return render(request, 'new_post.html', context={'form': form})

class PostUpdate(generic.UpdateView):
    template_name = 'new_post.html'
    form_class = NewPostForm
    context_object_name = 'data'
    model = models.Post

    def get_success_url(self):
        return reverse('post_list')

def post_delete(request, pk):
    data = models.Post.objects.get(pk=pk)
    data.delete()

    return redirect("post_list")

# class PostDelete(generic.TemplateView):
#     template_name = 'home.html'
#     model = models.Post
#
#     def get_success_url(self):
#         return reverse('post_list')