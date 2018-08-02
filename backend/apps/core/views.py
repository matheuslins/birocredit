from django.shortcuts import render
from rest_framework import generics

from .models import Pessoa
from apps.pessoa.serializer import PessoaSerializer


class ScoreDetalheView(generics.RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer = PessoaSerializer
