from django.urls import path
from .views import (
    PRODUCTDETAILVIEW,
    add_to_cart
)


urlpatterns = [
    path('product/<slug:slug>', PRODUCTDETAILVIEW.as_view(), name="single-product"),
    path('add-to-cart/<slug:slug>', add_to_cart, name="add-to-cart")
]
