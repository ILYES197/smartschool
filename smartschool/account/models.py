from django.db import models
from django.contrib.auth.models import User
import uuid  # تأكد من استيراد مكتبة uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid  # ✅ إضافة استيراد uuid

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    
    account_number = models.CharField(max_length=50, unique=True)  # رقم الحساب التجاري
    account_type = models.CharField(max_length=50)  # نوع الحساب التجاري
    first_name = models.CharField(max_length=100)  # الاسم الأول
    last_name = models.CharField(max_length=100)  # اللقب
    address = models.CharField(max_length=255)  # العنوان
    birth_date = models.DateField(null=True, blank=True)  # السماح بالقيم الفارغة
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # الرصيد المالي
    transfer_count = models.IntegerField(default=0)  # عدد مرات التحويل
    referral_link = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # رابط الإحالة الفريد

    def __str__(self):
        return f"{self.user.id} - {self.first_name} {self.last_name}"

    def get_referral_link(self):
        """إرجاع رابط الإحالة الخاص بالمستخدم"""
        return f"https://futuresite.online/register/?ref={self.referral_link}&user={self.user.username}"

# 🔹 إنشاء الملف الشخصي تلقائيًا عند إنشاء المستخدم
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            account_number=f"ACC-{uuid.uuid4().hex[:10]}",  # رقم حساب عشوائي
            account_type="Basic",  # نوع الحساب الافتراضي
            first_name=instance.first_name or "N/A",
            last_name=instance.last_name or "N/A",
            address="Unknown",
            birth_date="2000-01-01",  # تاريخ افتراضي
        )
    else:
        instance.profile.save()  # تحديث الملف الشخصي عند تعديل المستخدم

