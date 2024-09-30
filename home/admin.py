from django.contrib import admin
from .models import Category
from .models import Products
from .models import Order
from .models import OrderItem
from .models import Cart
from .models import CartItem
from .models import Payment
from .models import ShipAddress
from .models import Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(ShipAddress)
admin.site.register(Review)

