from django import forms
from .models import Cart

# write code here


class CartForm(forms.Form):

    quantity = forms.CharField(max_length=10)