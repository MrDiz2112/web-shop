from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string


def OrderCreate(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/paid.html', {'order': order})

    form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})


def OrderCreated(request):
    try:
        order_id = request.GET['order-id']
    except:
        order_id = None

    return render(request, 'orders/order/created.html', {'order_id': order_id})
