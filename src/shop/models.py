from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


PRODUCT_CATEGORY = (
    ('M&C', 'Mobiles & Computers'),
    ('MF', 'Men\s Fashion'),
    ('WF', 'Women\s Fashion'),
    ('H', 'Home'),
    ('B', 'Beauty')
)


PRODUCT_SIZE = (
    ('NONE', 'NONE'),
    ('S', 'small'),
    ('XS', 'extra small'),
    ('M', 'medium'),
    ('L', 'large'),
    ('XL', 'extra large'),
)

CUSTOMER_GENDER = (
    ('NONE', 'NONE'),
    ('M', 'male'),
    ('F', 'female'),
)

# Create your models here.


class Item(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    category = models.CharField(
        max_length=100, choices=PRODUCT_CATEGORY, default='H')
    compositions = models.CharField(max_length=100)
    size = models.CharField(
        max_length=50, choices=PRODUCT_SIZE, default='NONE')
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_preview = models.ImageField(upload_to="static/assets/upload")
    exclusive = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10, choices=CUSTOMER_GENDER, default='NONE')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("single-product", kwargs={"slug": self.slug})


    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

        


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
