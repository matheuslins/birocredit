from django.urls import path, include
from .views import PessoaDetalheView, ScoreDetalheView, EventosDetalheView


urlpatterns = [
    path(
        '/pessoas/<int>',
        PessoaDetalheView.as_view(),
        name='pessoa-detalhe'
    ),
    path(
        '/scores/<int>',
        ScoreDetalheView.as_view(),
        name='score-detalhe'
    ),
    path(
        '/pessoas/<int>/eventos',
        EventosDetalheView.as_view(),
        name='eventos-detalhe'
    ),
]
