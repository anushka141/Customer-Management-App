from django.contrib import admin
from .models import Customer, Order, Product, Tag
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
