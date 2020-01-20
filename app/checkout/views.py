from django.shortcuts import render
from django.views.generic import View
from .models import Checkout
from shop.models import Product, Cart
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

# simple function view for checkout
# def checkout(request):
#     return render(request, 'checkout.html', {})


# class based view
class checkOutView(View):

    def get(self, *args, **kwargs):

        try:

            item = Product.objects.get(slug=self.kwargs.get('slug'))

            context = {
                'item': item
            }

            return render(self.request, 'checkout.html', context)

        except ObjectDoesNotExist:
            messages.WARNING(self.request, 'This item does not exist')
