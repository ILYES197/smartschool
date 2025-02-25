import uuid
from django.db import models
from django.contrib.auth.models import User

class حساب_تجاري(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ربط الحساب التجاري بالمستخدم
    رقم_الحساب = models.CharField(max_length=50, unique=True)  # رقم الحساب التجاري
    نوع_الحساب = models.CharField(max_length=50)  # نوع الحساب التجاري
    الاسم = models.CharField(max_length=100)  # اسم الحساب
    اللقب = models.CharField(max_length=100)  # اسم الحساب
    العنوان = models.CharField(max_length=255)  # العنوان
    تاريخ_الميلاد = models.DateField()  # تاريخ الميلاد
    الرصيد_المالي = models.DecimalField(max_digits=15, decimal_places=2)  # الرصيد المالي
    عدد_مرات_التحويل = models.IntegerField(default=0)  # عدد مرات التحويل
    رابط_الإحالة = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # رابط الإحالة الفريد

    def __str__(self):
        return f"{self.الاسم} - {self.رقم_الحساب}"

    def get_رابط_الإحالة(self):
        """إرجاع رابط الإحالة مع اسم المستخدم"""
        return f"https://futuresite.online/register/?ref={self.رابط_الإحالة}&user={self.user.username}"
    