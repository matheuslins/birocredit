from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

import pessoa
from pessoa.serializer import (PessoaSerializer, EnderecoSerializer,
                               BemSerializer)


class EnderecoListCreateView(generics.ListCreateAPIView):
    queryset = pessoa.models.Endereco.objects.all()
    serializer_class = EnderecoSerializer


class BensListCreateView(generics.ListCreateAPIView):
    queryset = pessoa.models.Bem.objects.all()
    serializer_class = BemSerializer


class ScoreDetalheView(generics.RetrieveAPIView):
    model = pessoa.models.Pessoa
    endereco = pessoa.models.Endereco
    bem = pessoa.models.Bem
    lookup_field = 'cpf'

    def get(self, request, cpf):
        pessoa = self.model.objects.get(cpf=cpf)
        endereco = self.endereco.objects.filter(pessoa_endereco__cpf=cpf)
        bens = self.bem.objects.filter(pessoa=pessoa)
        score_pessoa = {
            'nome': pessoa.nome,
            'cpf': cpf,
            'endereco': EnderecoSerializer(endereco, many=True).data[0],
            'idade': pessoa.idade,
            'bens': BemSerializer(bens, many=True).data,
            'fonte_renda': pessoa.fonte_renda
        }
        return Response(score_pessoa)
