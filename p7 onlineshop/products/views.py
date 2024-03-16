from django.shortcuts import render
from django.views import generic

from .forms import CommentForm
from products.models import Product
from django.utils.translation import activate, get_language
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse

from django.contrib import messages
from cart.forms import CartAddForm

from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
    model = Product
    # queryset = Product.objects
    template_name = 'index.html'
    context_object_name = 'data'
    paginate_by = 5



    def get_queryset(self):
        print(self.request.path_info)
        return super().get_queryset()

# class ProductDetailView(generic.DetailView, generic.CreateView):
#     model = Product
#     template_name = 'product_detail.html'
#     context_object_name = 'data'
#     form_class = CommentForm
#
#     def form_valid(self, form):
#         form = form.save(commit=False)
#         form.author = self.request.user
#         form.product = self.get_object()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('product_detail', args=[self.kwargs['pk']])

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = form.save(commit=False)
            form.product = product
            form.author = request.user
            form.save()
        else:
            raise PermissionDenied

    form = CommentForm()
    context = {'data': product, 'form': form, 'cart_form': CartAddForm()}

    return render(request, 'product_detail.html', context=context)


def switch_lang(request, pk=None):
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        # request.session['django_language'] = lang_code  # Store language preference in session
        activate(lang_code)
        # res = HttpResponse()
        # res.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        # request.LANGUAGE_CODE = get_language()
        # rend = render(request, 'index.html')
        # rend.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

        rend = redirect('index')
        rend.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)


    return rend


def msg(request):
    messages.success(request, 'hellow')
    messages.warning(request, 'hellow')
    messages.error(request, 'hellow', extra_tags='danger')
    # request.COOKIES.update({settings.LANGUAGE_COOKIE_NAME :'en'})

    print(request.COOKIES)
    print(request.META)
    # request.session.update({'name':'ali'})
    r = render(request, 'test.html')
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    return r