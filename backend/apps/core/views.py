from django.shortcuts import render
from rest_framework import generics

from .models import Pessoa, Evento, Score
from .serializer import PessoaSerializer, EventoSerializer, ScoreSerializer


class PessoaDetalheView(generics.RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer = PessoaSerializer


class ScoreDetalheView(generics.RetrieveAPIView):
    queryset = Score.objects.all()
    serializer = ScoreSerializer


class EventosDetalheView(generics.RetrieveAPIView):
    queryset = Evento.objects.all()
    serializer = EventoSerializer
