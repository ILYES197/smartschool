from rest_framework import serializers
from .models import formation
<<<<<<< HEAD
=======
from .models import Comment
>>>>>>> 7cb928f279a365f5e97b4268eb287317d67d7e1e

class FormationSerializer(serializers.ModelSerializer):
     class Meta:
        model = formation
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # استخدام دالة مخصصة لجلب الاسم

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.get_full_name() if obj.user else "مجهول"
>>>>>>> 7cb928f279a365f5e97b4268eb287317d67d7e1e
