from django.urls import path
from .views import (
    PRODUCTVIEW,
    PRODUCTDETAILVIEW
)


urlpatterns = [
    path('products', PRODUCTVIEW.as_view(), name="products"),
    path('product/<slug:slug>', PRODUCTDETAILVIEW.as_view(), name="single-product")
]
