from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        #Criptografar a senha antes de salvar o usuário
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = '__all__'

class PatrimonioSerializer(serializers.Serializer):
    class Meta:
        model = Patrimonios
        fields = '__all__'

class AmbienteSerializer(serializers.Serializer):
    class Meta:
        model = Ambientes
        fields = '__all__'


class FuncionarioSerializer(serializers.Serializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'


class AreaSerializer(serializers.Serializer):
    class Meta:
        model = Area
        fields = '__all__'        