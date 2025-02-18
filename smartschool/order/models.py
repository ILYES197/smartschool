from django.db import models
from operator import mod 
from django.contrib.auth.models import User
from formation.models import formation


class Order(models.Model):
    
    city = models.CharField(max_length=400, default="", blank=False)
    academic_year = models.CharField(max_length=100, default="", blank=False)
    country = models.CharField(max_length=100, default="", blank=False)
    phone_number = models.CharField(max_length=100, default="", blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createAt = models.DateTimeField(auto_now_add=True) 
  #  total_amount = models.IntegerField( default=0 )

    def __str__(self):
        return str(self.id)
    
    
class OrderItem(models.Model):
    formation = models.ForeignKey(formation, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE,related_name='orderitems')
    name = models.CharField(max_length=200, default="", blank=False)
    price = models.DecimalField( max_digits=7, decimal_places=2,blank=False )
    status = models.CharField(max_length=50, default="pending", blank=False)

    

    def __str__(self):
        return self.name
