from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from .models import OrderItem, Order
from django.contrib.auth import get_user_model

from payments.IDPAY.idpay import IdPay
from .models import Order
from django.shortcuts import redirect

@login_required
def checkout(request):
    form = OrderForm(request.POST or None, initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    })
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            form = form.save(commit=False)
            form.user = request.user
            cart = Cart(request)
            form.total_price = cart.get_total_price()
            form.save()
            for i in cart:
                OrderItem.objects.create(order=form,
                                         product=i['obj'],
                                         quantity=i['quantity'],
                                         price=i['obj'].price)
            cart.clear()
            get_user_model().objects.update(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'])

            request.session['order_id'] = form.pk
            return redirect('payment_process')

    context = {'form': form}
    return render(request, 'checkout.html',context=context)

