# Register your models here.
from django.contrib import admin

from .models import Product
from .models import Contact,Order,OrderUpdate
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)

