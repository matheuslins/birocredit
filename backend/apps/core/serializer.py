from rest_framework import serializers

from .models import Consulta, Compra, Evento, Movimentacao


class BiroField(serializers.RelatedField):
    def to_representation(self, value):
        return {'nome': value.nome, 'site': value.site}


class ConsultaSerializer(serializers.ModelSerializer):
    biro = BiroField(read_only=True)

    class Meta:
        model = Consulta
        exclude = ('id',)


class CompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compra
        exclude = ('id', 'pessoa')


class MovimentacaoSerializer(serializers.ModelSerializer):
    tipo = serializers.SerializerMethodField()

    class Meta:
        model = Movimentacao
        fields = ('tipo', 'valor')

    def get_tipo(self, obj):
        return obj.get_tipo_display()


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        exclude = ('id',)
