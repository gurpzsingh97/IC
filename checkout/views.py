from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, 'There is nothing in your bag!')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form':order_form,
        'stripe_public_key': 'pk_test_51KWl26Emg8ueC1eqp3DpFyfnhhd4iD0I1Ymd60002m2WHGE4flw1ccu3QIPEz4zNutN6J86Sg4bTy9eoRojBY6Rx00p2IKcaHR',
        'client_secret':'sk_test_51KWl26Emg8ueC1eqDzFQJVzpgCaTwAw27md5J8dTkZ1WX11cojSHEV2X0xIEHQ4ocVzkPFCe1cPjVsKXlaXIZZKt004MALUlY1'
    } 

    return render(request, template, context)
