from rest_framework import serializers
from .models import formation
from .models import Comment

class FormationSerializer(serializers.ModelSerializer):
     class Meta:
        model = formation
        fields = "__all__"
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # إظهار اسم المستخدم بدلًا من ID

    class Meta:
        model = Comment
        fields = '__all__'