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
from .models import CustomUser

@api_view(['POST'])
def register(request):
    data = request.data
    user = SingUpSerializer(data=data)

    if user.is_valid():
        if not CustomUser.objects.filter(phone_number=data['phone_number']).exists():
            user = CustomUser.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'], 
                phone_number=data['phone_number'], 
                username=data['phone_number'], 
                password=make_password(data['password']),
            )
            return Response(
                {'details': 'Your account registered successfully!'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error': 'This phone number already exists!'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)
