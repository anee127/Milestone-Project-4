from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "nothing in bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KW0lOB9lojXCdzPROAEFkWj3ljl6JAHckh8370rXGrZXgsPuKwo8dAOGm3gFJskuiIcb1eIk9woJ8WCHgrE8Ncf00MJwzIqjr',
        'client_secret': 'test client secret',  
    }
           
    return render(request, template, context)
