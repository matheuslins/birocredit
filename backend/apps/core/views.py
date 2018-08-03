from django.shortcuts import render
from rest_framework import generics

from pessoa.models import Pessoa
from aplications.pessoa.serializer import PessoaSerializer


class ScoreDetalheView(generics.RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer = PessoaSerializer
