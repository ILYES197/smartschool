from rest_framework import serializers
from django.contrib.auth.models import User
 
from .models import حساب_تجاري

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
        
   

class حساب_تجاري_سيريالايزر(serializers.ModelSerializer):
    رابط_الإحالة_كامل = serializers.SerializerMethodField()  # إضافة رابط الإحالة الكامل

    class Meta:
        model = حساب_تجاري
        fields = [
            'user', 'رقم_الحساب', 'نوع_الحساب', 'الاسم', 'اللقب', 'العنوان',
            'تاريخ_الميلاد', 'الرصيد_المالي', 'عدد_مرات_التحويل', 'رابط_الإحالة', 'رابط_الإحالة_كامل'
        ]
        read_only_fields = ['رقم_الحساب', 'نوع_الحساب', 'الرصيد_المالي', 'عدد_مرات_التحويل']

    def get_رابط_الإحالة_كامل(self, obj):
        return obj.get_رابط_الإحالة()


