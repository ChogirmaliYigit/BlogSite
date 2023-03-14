from django.contrib import admin
from .models import Category, Food, Order, OrderItem, Client


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(OrderItem)
admin.site.register(Client)

