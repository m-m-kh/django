from django.shortcuts import render
from order.models import Order
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse
from .IDPAY.idpay import IdPay
from .models import TransactionModel
from django.views.decorators.http import require_GET

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, pk=int(order_id))

    idpay = IdPay('087fdd57-5d41-4ecd-b39a-53b9634d0579',True)
    transaction = idpay.create_transaction(order_id, order.total_price*10,
                                           'localhost.com/confirm_payment')
    TransactionModel.objects.create(id=transaction['id'],link=transaction['link'],
                                    amount=order.total_price,
                                    order_id=order_id,
                                    to_order=order)
    return redirect(transaction['link'])

@require_GET
def confirm_payment(request):
    status = request.GET.get('status')
    id = request.GET.get('id')
    order_id = request.GET.get('order_id')

    idpay = IdPay('087fdd57-5d41-4ecd-b39a-53b9634d0579',True)
    if status == '10':
        response = idpay.verify_transaction(id=id, order_id=order_id)
        if response.get('error_code'):
            return HttpResponse('its too late')
        if response['status'] == 100:
            transaction_model = get_object_or_404(TransactionModel, id=response['id'])
            transaction_model.status = response['status']
            transaction_model.track_id = response['track_id']
            transaction_model.card_no = response['payment']['card_no']
            transaction_model.hashed_card_no = response['payment']['hashed_card_no']
            transaction_model.save()
            # pass
            HttpResponse('confirmed')
        elif response['status'] == 101:
            HttpResponse('already confirmed')
    else:
        HttpResponse('rejected transaction')

    # < QueryDict: {'status': ['10'], 'track_id': ['1348151'], 'id': ['1244600b7f408796c340fb4413eb43b4'],
    #               'order_id': ['28']} >

    return HttpResponse('ww')