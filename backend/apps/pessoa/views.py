from django.shortcuts import render
from django.forms.models import model_to_dict

from rest_framework import generics
from rest_framework.response import Response

from core.models import Compra, Consulta, Evento, Movimentacao
from core.serializer import (CompraSerializer, ConsultaSerializer,
                             EventoSerializer, MovimentacaoSerializer)
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer, BiroSerializer
from .mixins import CreateListMixin
from .models import Pessoa, Endereco, Divida
from .serializer import PessoaSerializer, EnderecoSerializer, DividaSerializer


class PessoaListCreateView(CreateListMixin, generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaDetalheView(generics.RetrieveAPIView):
    lookup_field = 'cpf'

    def get(self, request, cpf):
        pessoa = Pessoa.objects.get(cpf=cpf)
        endereco = Endereco.objects.filter(pessoa_endereco__cpf=cpf)
        dividas = Divida.objects.filter(pessoa=pessoa)
        dados_pessoa = {
            'nome': pessoa.nome,
            'cpf': pessoa.cpf,
            'endereco': EnderecoSerializer(endereco, many=True).data[0],
            'dividas': DividaSerializer(dividas, many=True).data,
        }
        return Response(dados_pessoa)


class EventosDetalheView(generics.ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    lookup_field = 'cpf'

    def get(self, request, cpf):
        pessoa = Pessoa.objects.get(cpf=cpf)
        eventos = Evento.objects.filter(pessoa=pessoa)
        evento_serializer = EventoSerializer(eventos, many=True).data

        list_eventos = []
        for evento in evento_serializer:
            consulta = Consulta.objects.filter(
                id=evento['consulta']).latest('data')
            compra = Compra.objects.filter(pessoa=pessoa).last()
            movimentacoes = Movimentacao.objects.filter(pessoa__cpf=cpf)
            list_eventos.append({
                'cpf': pessoa.cpf,
                'ultima_consulta': ConsultaSerializer(consulta).data,
                'movimentacoes': MovimentacaoSerializer(
                    movimentacoes, many=True).data,
                'ultima_compra_cartao': CompraSerializer(compra).data
            })

        return Response(list_eventos)
