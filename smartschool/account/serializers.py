from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Profile
from .models import TransferRequest


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
        
# serializers.py
from rest_framework import serializers
from account.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['birth_date', 'address']  # هنا حدد غير الحقول لي تحب تحدثهم
        
        
 
class TransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = '__all__'   
        read_only_fields = ['id', 'created_at']  # جعل بعض الحقول للقراءة فقط

 
