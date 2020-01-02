from .models import Tenista
from .models import Asignado
from rest_framework import serializers

class TenistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenista 
        fields = '__all__'

class AsignadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asignado
		fields = '__all__'
