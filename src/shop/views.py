from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse, Http404
from .models import Item, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


# class view for single product
class PRODUCTDETAILVIEW(DetailView):

    def get(self, *args, **kwargs):

        item = Item.objects.get(slug=self.kwargs.get('slug'))

        context = {
            'item': item
        }

        return render(self.request, 'product-page.html', context)


def add_to_cart(request, slug):

    try:

        item = get_object_or_404(Item, slug=slug)

        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )

        print('this is the order item')
        print(order_item)

        order_qs = Order.objects.filter(user=request.user, ordered=False)

        if order_qs.exists():

            # user already added item, add more items
            print('yeehhhh it is already existed')

            messages.info(
                request, "user already added items in their cart and adding more ")

        else:
            # create order of new user
            order = Order.objects.create(user=request.user)
            order.items.add(order_item)

            messages.info(request, "This item was added to your cart")

            return redirect('/summary')

        return redirect('/summary')

    except expression as error:

        print(error)

        return Http404('something is wrong...')
