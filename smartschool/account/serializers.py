from rest_framework import serializers
from django.contrib.auth.models import User
#from  .models import CustomUser  

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ('first_name','last_name', 'email', 'password'  )

        extra_kwargs = {
            'first_name': {'required':True ,'allow_blank':False},
            'last_name' : {'required':True ,'allow_blank':False},
            'email' : {'required':False ,'allow_blank':True},
            'password' : {'required':True ,'allow_blank':False,'min_length':8},
           # 'phone_number': {'required': True, 'allow_blank': False},
             
        } 
        
class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model =  User
        fields = ('first_name','last_name', 'email', 'username' ) 