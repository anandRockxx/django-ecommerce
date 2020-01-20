from django.urls import path
from .views import checkOutView

urlpatterns = [
    path('product/<slug:slug>/checkout', checkOutView.as_view(), name="checkout")
]

