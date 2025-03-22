from django.contrib import admin
 
from .models import Profile
from .models import TransferRequest
# Register your models here.
admin.site.register(Profile)
admin.site.register(TransferRequest)
 