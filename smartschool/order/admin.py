from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.site_header = 'future site'
admin.site.site_title = 'future site'
