from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SingUpSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from .models import CustomUser
from .models import حساب_تجاري
from .serializers import حساب_تجاري_سيريالايزر
 


@api_view(['POST'])
def register(request):
    data = request.data
    user = SingUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'], 
                email = data['email'] , 
                #phone_number=data['phone_number'] , # إضافة رقم الهاتف
                username = data['email'] , 
                password = make_password(data['password']),
            )
            return Response(
                {'details':'Your account registered susccessfully!' },
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'eroor':'This email already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)


from rest_framework import viewsets, permissions
from .models import حساب_تجاري
from .serializers import حساب_تجاري_سيريالايزر

class حساب_تجاري_ViewSet(viewsets.ModelViewSet):
    queryset = حساب_تجاري.objects.all()
    serializer_class = حساب_تجاري_سيريالايزر
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """يستطيع المستخدم مشاهدة حسابه فقط، بينما الـ admin يمكنه مشاهدة الجميع"""
        if self.request.user.is_staff:
            return حساب_تجاري.objects.all()
        return حساب_تجاري.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """عند إنشاء الحساب، يتم ربطه بالمستخدم الحالي"""
        serializer.save(user=self.request.user)
