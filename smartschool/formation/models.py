from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.TextChoices):
    إبتدائي = 'ابتداءي '
    متوسط = 'متوسطة'
    ثانوي = 'ثانوي'
    جامعة = 'جامعة'
    المتجر = 'المتجر'
    متنوعةدورات= 'دورات متنوعة'
     
    
class formation(models.Model):
     name = models.CharField(max_length=200,default="",blank=False)
     prof = models.CharField(max_length=200,default="",blank=False)
     description = models.TextField(max_length=1000,default="",blank=False) 
     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
     module = models.CharField(max_length=200,default="",blank=False)
     category = models.CharField(max_length=60, choices =category.choices )
     image = models.FileField(upload_to='formation_images')
     link = models.TextField(max_length=1000,default="",blank=False) 
     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
     def __str__(self):
        return self.name
     
 