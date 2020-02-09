from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from shop.models import Item, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from shop.models import Item, Order, OrderItem







# summary view
class OrderSummaryView(View):

    def get(self, *args, **kwargs):

        try:

            summary_cart = Order.objects.get(
                user=self.request.user, ordered=False)

            context = {
                'object': summary_cart
            }

            print(context)

            return render(self.request, 'order-summary.html', context)

        except ObjectDoesNotExist:

            messages.warning(self.request, "You do not have an active order")
            return redirect("/")





# check out view
class CheckOutView(View):

    def get(self, *args, **kwargs):

        try:

            # item = Product.objects.get(slug=self.kwargs.get('slug'))

            # context = {
            #     'item': item
            # }

            return render(self.request, 'checkout-page.html', {})

        except ObjectDoesNotExist:
            messages.WARNING(self.request, 'This item does not exist')
