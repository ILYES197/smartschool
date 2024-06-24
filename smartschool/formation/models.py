from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Category(models.TextChoices):
   # SCIENCE = 'Science'
   # PHYSIQUE = 'Physique'
   # MATHEMATIQUE = 'Mathématique'
     
    
class formation(models.Model):
     name = models.CharField(max_length=200,default="",blank=False)
     prof = models.CharField(max_length=200,default="",blank=False)
     description = models.TextField(max_length=1000,default="",blank=False) 
     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
     module = models.CharField(max_length=200,default="",blank=False)
     category = models.CharField(max_length=40,default="",blank=False )
     image = models.FileField(upload_to='formation_images')
     link = models.TextField(max_length=1000,default="",blank=False) 
     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
     def __str__(self):
        return self.name
     
 