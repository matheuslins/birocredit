from django.shortcuts import render
from rest_framework import generics

from .models import Score
from .serializer import ScoreSerializer


class ScoreDetalheView(generics.RetrieveAPIView):
    queryset = Score.objects.all()
    serializer = ScoreSerializer
