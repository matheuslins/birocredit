from rest_framework import serializers

from empresa.serializers import EmpresaSerializer
from .models import Bem, Divida, Endereco, Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class BemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bem
        fields = '__all__'


class DividaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    total = serializers.SerializerMethodField()
    tipo = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Divida
        exclude = ('id', 'pessoa')

    def get_total(self, obj):
        return obj.valor + obj.juro

    def get_tipo(self, obj):
        return obj.get_tipo_display()

    def get_status(self, obj):
        return obj.get_status_display()
