from django.urls import path
from .views import CheckOutView, OrderSummaryView




urlpatterns = [

    path('summary', OrderSummaryView.as_view(), name="summary"),
    path('checkout', CheckOutView.as_view(), name="checkout")

]

