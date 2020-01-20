from django.forms import forms
from .models import Cart

# write code here


class CartForm(forms.Form):
    class Meta:
        model = Cart
        fields = [
            'title', 'quantity'
        ]
