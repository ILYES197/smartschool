from django.contrib import admin
from  .models import formation 
from  .models import Comment
# Register your models here.
admin.site.register(formation)
admin.site.register(Comment)