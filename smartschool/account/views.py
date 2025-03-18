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
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import TransferRequest
from .serializers import TransferRequestSerializer


@api_view(['POST'])
def register(request):
    data = request.data
    user_serializer = SingUpSerializer(data=data)

    if user_serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['email'],
                password=make_password(data['password']),
            )

            # نحاول نجيب ref من الرابط (من ال request)
            referral_code = data.get('referral_code')  # ممكن تجيه من الفورم أو رابط
            if referral_code:
                try:
                    referred_profile = Profile.objects.get(referral_link=referral_code)
                    user.profile.referred_by = referred_profile.user
                    user.profile.save()
                except Profile.DoesNotExist:
                    pass  # إذا كان referral code خطأ، نتجاهلو

            referral_link = user.profile.get_referral_link()

            return Response(
                {
                    'details': 'Your account registered successfully!',
                    'referral_link': referral_link
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error': 'This email already exists!'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET' , 'PUT'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)

# views.py 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer, ProfileUpdateSerializer


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response({"detail": "Profile does not exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileUpdateSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



 

class TransferRequestViewSet(viewsets.ModelViewSet):
    queryset = TransferRequest.objects.all().order_by('-created_at')  # ترتيب الطلبات من الأحدث إلى الأقدم
    serializer_class = TransferRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # السماح بعرض الطلبات للجميع ولكن التعديل يحتاج إلى تسجيل دخول

    def perform_create(self, serializer):
        """حفظ الطلب مع تاريخ الإنشاء تلقائيًا"""
        serializer.save()