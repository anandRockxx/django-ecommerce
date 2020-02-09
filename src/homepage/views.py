from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from shop.models import Item


class Index(View):

    def get(self, *args, **kwargs):

        try:

            # latest_qs = Item.objects.latest('created_at')

            # # latest_qs = Item.objects.get(title = latest_item)
            # exclusive_qs = Item.objects.filter(exclusive = True)

            # context = {
            #     'latest': latest_qs,
            #     'execlusive': exclusive_qs
            # }

            qs = Item.objects.all()


            return render(self.request, 'home-page.html', {"items": qs})

        except Exception as e:

            print(e)

            return render(self.request, '404.html', {})

            

        
