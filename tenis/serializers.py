from .models import Tenista
from .models import Asignado
from .models import Partido
from rest_framework import serializers

class TenistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenista 
        fields = '__all__'

class AsignadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asignado
		fields = '__all__'

class PartidoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partido
		fields = '__all__'