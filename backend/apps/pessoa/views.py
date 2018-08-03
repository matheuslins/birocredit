from django.shortcuts import render
from rest_framework import generics

from core.models import Evento
from .models import Pessoa
from .serializer import PessoaSerializer, EventoSerializer


class PessoaDetalheView(generics.RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer = PessoaSerializer


class EventosDetalheView(generics.RetrieveAPIView):
    queryset = Evento.objects.all()
    serializer = EventoSerializer
