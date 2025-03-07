from rest_framework import serializers
from .models import formation
from .models import Comment

class FormationSerializer(serializers.ModelSerializer):
     class Meta:
        model = formation
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # استخدام دالة مخصصة لجلب الاسم

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.get_full_name() if obj.user else "مجهول"