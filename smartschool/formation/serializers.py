from rest_framework import serializers
from .models import formation

class FormationSerializer(serializers.ModelSerializer):
     class Meta:
        model = formation
        fields = "__all__"