from .models import Tenista
from rest_framework import serializers

class TenistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenista 
        fields = '__all__'
