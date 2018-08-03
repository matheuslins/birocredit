from rest_framework import serializers
from django.forms.models import model_to_dict

from .models import Empresa, Biro


class EmpresaSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        new_representation = model_to_dict(value)
        new_representation.pop('id')
        return new_representation

    class Meta:
        model = Empresa
        exclude = ('id',)


class BiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biro
        exclude = ('id',)
