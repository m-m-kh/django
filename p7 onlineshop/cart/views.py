from itertools import product

from django.shortcuts import render
from django.views.decorators.http import require_POST
from products.models import Product
from . import forms
# Create your views here.
from django.shortcuts import redirect
from .cart import Cart

from django.http import Http404
from django.shortcuts import get_object_or_404

from django.core.exceptions import BadRequest
from .forms import CartAddForm
from django.contrib import messages
def cart_list(request):
    cart = Cart(request)
    total = sum(product['obj'].price * product['quantity'] for product in cart)
    context = {'cart': cart, 'form': forms.CartAddForm(), 'total': total}
    print(request.session.load())
    return render(request, 'cart.html', context = context)


def add_cart(request, pk):
    form = forms.CartAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            cart = Cart(request)
            # cart.remove(pk)
            quantity = int(form.cleaned_data['quantity'])
            cart.add(pk, quantity)
            messages.success(request, 'با موفقیت اضافه شد')
        else:
            raise Http404

    return redirect('cart_list')
    # return redirect(request.META.get('HTTP_REFERER'))

def update_cart(request, pk):
    form = CartAddForm(request.POST)
    if form.is_valid() and get_object_or_404(Product, pk=pk):
        cart = Cart(request)
        cart.update(pk, quantity=form.cleaned_data['quantity'])
        messages.warning(request, 'با موفقیت تغییر کرد')
    else:
        raise Http404
    # get_object_or_404(Product, pk=pk)
    # if act == 'plus':
    #     cart = Cart(request)
    #     cart.add(pk, quantity=+1)
    # elif act == 'minus':
    #     cart = Cart(request)
    #     cart.add(pk, quantity=-1)
    # else:
    #     raise Http404

    return redirect('cart_list')
def remove_cart(request, pk):
    cart = Cart(request)
    cart.remove(pk)
    return redirect('cart_list')

def remove_all_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.clear()
        print(request.POST)
        return redirect('cart_list')
    raise BadRequest