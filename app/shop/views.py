from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse, Http404
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import CartForm


# class view for products
class PRODUCTVIEW(View):

    def get(self, *args, **kwargs):

        query = Product.objects.all()

        return render(self.request, 'products.html', {'products': query})


# class view for single product
class PRODUCTDETAILVIEW(DetailView):

    def get(self, *args, **kwargs):

        item = Product.objects.get(slug=self.kwargs.get('slug'))

        context = {
            'item': item
        }

        return render(self.request, 'single_product.html', context)

    def post(self, *args, **kwargs):

        try:

            form = CartForm(self.request or None)

            print(form)

            print('this is the post method...')

            return render(self.request, 'checkout.html', {})

        except ObjectDoesNotExist:
            messages.error(
                self.request, 'Something went wrong. Please retry again')
